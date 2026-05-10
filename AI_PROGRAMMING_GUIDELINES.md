# Advice from "I Have Spent 500+ Hours Programming With AI. This Is what I learned" by The Coding Sloth

**Core Philosophy:**  
AI is a powerful *multiplier* of your existing skills — **not a replacement** for thinking, planning, or foundational knowledge. It amplifies both good and bad engineering habits. The biggest gains come from clear communication, breaking problems down, providing context, and always verifying output.

### Key Tips & Advice (in video order):

1. **Learn how to program first**  
   - AI cannot outsource your brain.  
   - Without solid fundamentals, AI is useless (or even harmful).  
   - Master programming basics before leaning heavily on AI.

2. **Be as specific as humanly possible in your prompts**  
   - Vague prompts = poor results. Most people fail here because they lack strong communication skills.  
   - Include: tech stack, exact requirements, user flows, styling, screenshots, documentation links, terminal commands, etc.  
   - Experiment example: "Build Google Docs" (fails) vs. fully detailed prompt with everything specified (works almost perfectly).  
   - Pro tip: Ask AI to *improve* your own prompt using best practices.

3. **Use AI alongside traditional research (Google + docs)**  
   - Don’t replace Google — feed documentation and solutions directly into AI.  
   - Saves time copying/pasting context.

4. **Break big tasks into small, well-defined ones**  
   - AI excels at small pieces, not massive vague projects.  
   - Plan the architecture yourself, then let AI execute the pieces.  
   - If you can’t break it down, you don’t understand the problem well enough yet.

5. **Use the 3-section prompt pattern to reduce "slop"**  
   - **Task** (highly descriptive)  
   - **Background Info** (files, docs, images, user flow, styling)  
   - **Do Not / Constraints** section (what not to change, what to avoid)  
   - Dramatically improves consistency and quality.

6. **Create guidelines / rules files**  
   - Make a `guidelines.md` or `agents.md` in your project.  
   - Include: project overview, tech stack, important commands, coding standards, workflow.  
   - AI can auto-generate this by analyzing your codebase.  
   - Reference it in every prompt for consistency.

7. **Leverage Model Context Protocol (MCP) tools**  
   - These give AI live access to your project (docs, app state, errors, logs, browser dev tools, etc.).  
   - Recommended examples (for web dev): Context7, Next.js Developer Tools, Chrome DevTools.  
   - Huge quality boost — find MCPs for your specific tech stack.

8. **Always provide a way for AI to verify its own work**  
   - Don’t just ask for code — ask it to include tests, run commands, or verification steps.  
   - You (or the AI) should actually run and check the output.

9. **AI amplifies your engineering habits**  
   - Good habits (planning, testing, documentation, verification) → massive wins.  
   - Bad habits (no tests, ignoring edge cases) → amplified disasters.  
   - Be over-prepared and deliberate.

### Final Takeaways:
- Be "productively lazy": Let AI handle the typing/implementation, **never** the thinking/architecture.  
- Treat AI like a very fast junior developer who needs extremely clear instructions and supervision.  
- Review everything AI produces — don’t blindly copy.  
- The difference between "AI is magic" and "AI is useless" is almost entirely in **how you communicate and structure your workflow**.

**Sponsored tool mentioned:** Junie by JetBrains (great prompts, templates, and safeguards).

*Source: Full video transcript summary from https://www.youtube.com/watch?v=91B_v-wOaws*
