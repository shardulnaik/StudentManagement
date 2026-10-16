@'
# Student Management Platform

A full-stack student management platform built with **Flask**, **Vue.js**, and **MySQL** for managing student information through a structured web application.

## Overview

The Student Management Platform provides a centralized interface for managing student records and interacting with a backend REST API backed by MySQL.

The project demonstrates full-stack application development, REST API design, database integration, frontend-backend communication, configuration management, and maintainable project organization.

## Tech Stack

### Backend
- Python
- Flask
- REST API
- MySQL
- Python virtual environment

### Frontend
- Vue.js
- JavaScript
- HTML5
- CSS3

### Database
- MySQL

### Development & Tooling
- Git
- GitHub
- GitHub Actions
- Pytest
- Environment-based configuration

## Architecture

```text
┌─────────────────────────┐
│      Vue.js Frontend    │
│                         │
│  UI / Components / API  │
└────────────┬────────────┘
             │ HTTP
             ▼
┌─────────────────────────┐
│       Flask API         │
│                         │
│ Routes / Application    │
│ Logic / Data Models     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│         MySQL           │
│                         │
│     Student Data        │
└─────────────────────────┘