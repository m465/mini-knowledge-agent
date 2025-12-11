import json
import sys
from config import openai_client
from tools.schemas import tools_schema
from tools.registry import AVAILABLE_FUNCTIONS
from utils.logger import logger

def run_agent():
    print("🤖 Mini Knowledge Agent Initialized (Type 'exit' to quit)")
    print("-------------------------------------------------------")

    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to tools. Use them when needed."}
    ]

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            messages.append({"role": "user", "content": user_input})

            # 1. Send Query to OpenAI
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                tools=tools_schema,
                tool_choice="auto"
            )

            response_message = response.choices[0].message
            tool_calls = response_message.tool_calls

            # 2. Check if OpenAI wants to use a tool
            if tool_calls:
                messages.append(response_message) # Add the assistant's "intent" to history
                print(f"⚙️  Agent decided to use {len(tool_calls)} tool(s)...")

                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    if function_name in AVAILABLE_FUNCTIONS:
                        print(f"   -> Calling {function_name}...")
                        
                        # Call the actual function from registry
                        function_to_call = AVAILABLE_FUNCTIONS[function_name]
                        function_response = function_to_call(**function_args)
                        
                        # Add result to history
                        messages.append({
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        })
                    else:
                        print(f"   -> Error: Tool {function_name} not found.")

                # 3. Send Tool Results back to OpenAI for final answer
                final_response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages
                )
                print(f"🤖 Agent: {final_response.choices[0].message.content}")
                messages.append(final_response.choices[0].message)

            else:
                # No tools needed
                print(f"🤖 Agent: {response_message.content}")
                messages.append(response_message)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            logger.error(f"Critical Loop Error: {e}")

if __name__ == "__main__":
    run_agent()