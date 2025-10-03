# Wellness Tracker API
A backend API built with Django and Django REST Framework (DRF) to track movement, meditation, and morning pages activities. Designed to help users form and maintain healthy habits, inspired by BJ Fogg's Tiny Habits.

## Motivation

This project is motivated by the philosophy in Tiny Habits:

**“Make habits so small you can’t say no, then celebrate every success.”**

The goal of this API is to provide structured, trackable, and motivating feedback for personal wellness:

- Movement: Track running, cycling, yoga, or strength training.

- Meditation: Log duration, mood before/after, and music used.

- Morning Pages: Record completion, mood, word count, and time.

This project combines habit formation, reflection, and self-tracking into a single backend service.


## Features

- CRUD for Activities

  - Movement: duration, type, distance, notes
  
  - Meditation: duration, mood before/after, music, notes
  
  - Morning Pages: completed status, time, word count, mood, notes

## Goals

- Users can set goals for any activity type

- Track progress toward goals over a defined period

## Routines

- Users can create routines (combining activities) to follow consistently

- Optional active/inactive status

## Metrics & Analytics

- Total duration and distance for movement

- Total meditation minutes and mood trends

- Morning Pages completion streak

- Aggregated per user for dashboards


