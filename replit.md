# Discord AI Roast Bot

## Overview
A Discord bot that uses Google's Gemini AI to "roast" users on a Discord server. The bot automatically responds to every message with AI-generated responses.

## Project Structure
- `bot.py` - Main bot file containing Discord bot logic and Gemini AI integration
- `requirements.txt` - Python dependencies (discord.py, google-generativeai)
- `Proctfile` - Heroku/Railway worker configuration (legacy)

## Required Secrets
- `DISCORD_TOKEN` - Discord bot token from the Discord Developer Portal
- `GEMINI_API_KEY` - Google AI Gemini API key

## Bot Features
- Responds to all messages with AI-generated "roasts"
- Can be toggled on/off with "ai-start" and "ai-stop" commands
- Uses Gemini Pro model for text generation

## Running
The bot runs via the "Discord Bot" workflow which executes `python bot.py`.
