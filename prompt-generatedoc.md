## GitHub Copilot Agent Prompt: Aspire Solution Analysis & Documentation

1. **Launch the current solution** (a .NET Aspire Host).
   - If the application requires a token, ask the user to perform the login before proceeding.

2. **Analyze the entire solution** (all projects, code, and configuration files) to understand the overall goal and architecture.
3. **Analyze the AspireApp2.AppHost project** to generate an architecture diagram representing the solution's structure and service relationships. Include this diagram in the main documentation.
4. **Create a detailed Markdown file (`SolutionOverview.md`) that:**
   - Explains the goal and purpose of the solution.
   - Describes the architecture, main components, and their interactions.
   - Includes the generated architecture diagram.
   - Provides as much detail as possible about the solution’s design, features, and intended use.
5. **(Optional, only if user confirms)**: Use Playwright MCP server tools to:
   - Capture a screenshot of the Aspire dashboard.
   - Capture a screenshot of the main frontend page.
   - If Playwright MCP server tools can't launch the app, ask the user for the correct Aspire launch URL. By default, use: https://localhost:17187

**Instructions:**
- Ensure the markdown is well-structured, with sections for Overview, Architecture, Components, and Screenshots.
- Use the screenshots to visually illustrate the dashboard and frontend.
- Be thorough in your analysis and explanations.