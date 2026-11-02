# 📧 AI Mail Sender Agent

An AI-powered email automation project built using **n8n**. A chat-based AI agent reads data from **Google Sheets** and sends emails through **Gmail**, all driven by a simple conversation.

The project demonstrates how AI agents, tool calling, and workflow automation can be combined to reduce repetitive manual work and make email communication faster.

## 🚀 Project Overview

**AI Mail Sender** is an n8n workflow where the user chats with a "Data Analyst Agent". The agent understands the request, can look up rows from a connected Google Sheet, and can send an email using Gmail as a tool.

Instead of opening a spreadsheet, copying details and writing every email by hand, the user can simply type a request in the chat and let the AI agent do the work.

## ✨ Features

- 💬 **Chat Interface** — Public chat trigger with a friendly greeting and input placeholder.
- 🤖 **AI Agent** — An n8n AI Agent decides which tool to use based on the user's message.
- 🧠 **OpenAI Chat Model** — Uses `gpt-5-mini` as the language model.
- 🗂️ **Conversation Memory** — Simple Memory (window of the last 10 messages) keeps context between messages.
- 📊 **Google Sheets Integration** — Reads row(s) from a Google Sheet to fetch data.
- 📨 **Gmail Integration** — Sends emails directly from the agent using the Gmail tool.
- ⚙️ **Customizable** — Prompts, tools, and workflow logic can be modified easily.
- ⏱️ **Time Saving** — Reduces effort for repetitive email tasks.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **n8n** | Workflow automation platform |
| **Chat Trigger** | Receives the user's chat message |
| **AI Agent** | Orchestrates the model, memory and tools |
| **OpenAI Chat Model (gpt-5-mini)** | Understands requests and generates responses |
| **Simple Memory** | Stores recent conversation history (context window: 10) |
| **Google Sheets Tool** | Reads rows from a spreadsheet |
| **Gmail Tool** | Sends email messages |

## 🔄 Workflow Architecture

The workflow consists of 6 nodes:

1. **When chat message received** — Chat trigger that starts the workflow when the user sends a message.
2. **AI Agent** — Central node that processes the request and chooses the right tool.
3. **OpenAI Chat Model** — Language model connected to the agent (`gpt-5-mini`).
4. **Simple Memory** — Memory connected to the agent to remember recent messages.
5. **Get row(s) in sheet in Google Sheets** — Tool that reads data from the Google Sheet.
6. **Send a message in Gmail** — Tool that sends an email.

### Workflow Diagram

```text
        When chat message received
                   |
                   v
               AI Agent
                   |
   +---------------+----------------+----------------------+
   |               |                |                      |
   v               v                v                      v
OpenAI Chat     Simple          Google Sheets          Gmail
Model           Memory          (Get row(s))           (Send a message)
(Model)         (Memory)        (Tool)                 (Tool)
```

*The Chat Model, Memory, and the two tools are all sub-nodes connected to the AI Agent.*

## 📸 Screenshots

Add your screenshots in the `screenshots/` folder and reference them here:

```markdown
![Workflow Overview](screenshots/workflow-overview.png)
![OpenAI Chat Model Configuration](screenshots/openai-chat-model.png)
```

## 📩 Example

### Input (chat message)

```text
Check the sheet and send an email to the student about the pending work.
```

### What happens

1. The chat trigger receives the message.
2. The AI Agent reads the request and, if needed, calls the **Google Sheets** tool to fetch row data.
3. The agent then calls the **Gmail** tool to send the email.
4. The chat displays the final response from the agent.

*This is an illustrative example. Actual behavior depends on your prompt and node configuration.*

## ⚙️ Getting Started

### Prerequisites

- An n8n instance (cloud or self-hosted).
- An OpenAI API key, or n8n AI gateway credits.
- A Google account with access to Google Sheets and Gmail.
- A Google Sheet containing your data.

### Step 1: Import the Workflow

1. Open n8n and create a new workflow.
2. Click the **⋯** menu → **Import from File**.
3. Select `workflows/AI_mail_Sender.json`.

### Step 2: Configure Credentials

- **OpenAI** — Add your OpenAI credential in the *OpenAI Chat Model* node and select the model (`gpt-5-mini`).
- **Google Sheets** — Connect your Google account (OAuth2) and select your own spreadsheet and sheet.
- **Gmail** — Connect your Gmail account (OAuth2).

### Step 3: Configure the Gmail Node

In the exported workflow, the Gmail node uses fixed example values for the recipient, subject and message. Update these to your own, or click the ✨ button beside a parameter in n8n to let the AI fill it dynamically:

- **To:** Recipient's email address
- **Subject:** Email subject
- **Message:** Email body

### Step 4: (Recommended) Add a System Message to the AI Agent

For better results, add instructions in the AI Agent node, for example:

```text
You are a Data Analyst Agent.

Use the Google Sheets tool to read data when the user asks about it.
Use the Gmail tool to send professional, clear and polite emails
based on the information provided by the user.

Do not invent recipient details or factual information.
Confirm the recipient and content before sending when unsure.
```

### Step 5: Test the Workflow

1. Click **Open chat** in n8n.
2. Send a test message.
3. Verify that:
   - The agent reads the correct sheet data.
   - The email content is correct.
   - The email is delivered successfully.

Use a test email address before emailing real recipients.

## 🔐 Security and Best Practices

- Never upload API keys, passwords or OAuth credentials to GitHub. The exported JSON should contain only credential references, not secrets.
- Remove personal email addresses and private Google Sheet links from the JSON before making the repository public.
- Store credentials using n8n's credential manager.
- Verify recipient addresses before sending.
- Review AI-generated emails for accuracy.
- Test with sample data before enabling automated sending.
- Avoid sending unsolicited emails and follow your email provider's policies.

## 📂 Suggested Project Structure

```text
ai-mail-sender-n8n/
│
├── README.md
├── workflows/
│   └── AI_mail_Sender.json
├── screenshots/
│   ├── workflow-overview.png
│   └── openai-chat-model.png
└── .gitignore
```

## 🔮 Future Improvements

- Let the AI fill the Gmail recipient, subject and body dynamically.
- Add a structured output parser (subject and body in JSON).
- Personalized emails using spreadsheet data.
- Bulk email sending with sending limits.
- Human approval step before sending important emails.
- Email scheduling and follow-up automation.
- Input validation, error handling and execution logging.
- Support for more tools such as Google Calendar or Slack.

## 🎯 Use Cases

- Student reminders and status notifications.
- Professional business communication.
- Automated follow-up emails.
- Task or deadline reminders from a spreadsheet.
- Customer support responses.
- Routine administrative communication.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork this repository.
2. Create a new branch for your changes.
3. Implement and test your improvements.
4. Submit a pull request describing your changes.

## 📄 License

This project can be distributed under the MIT License. If you choose it, add a `LICENSE` file with the standard MIT License text and your copyright information.

## 👨‍💻 Author

**Sanskar Shejal**

GitHub: [Add your GitHub profile link here]

---

⭐ If you find this project useful, consider giving the repository a star!
