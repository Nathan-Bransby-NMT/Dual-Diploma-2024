  import 'package:flutter/material.dart';

class NewsPost {
  final String title;
  final String description;
  final DateTime date;

  final int maxDescriptionLength = 250;

  String content;
  DateTime? lastUpdated;

  NewsPost({
    required this.title,
    required this.description,
    required this.content,
    DateTime? date,
    DateTime? lastUpdated,
  }) : date = date ?? DateTime.now(); // Automatically Sets the date if the date is not provided.

  void updateContent(String newContent) {
    content = newContent;
    lastUpdated = DateTime.now();
  }

  int get remainingDescriptionCharacterCount {
    return maxDescriptionLength - description.length;
  }

  bool get isWithinCharacterRange {
    return maxDescriptionLength > remainingDescriptionCharacterCount && remainingDescriptionCharacterCount > 0;
  }

  set description(newDescription) {
    if (!isWithinCharacterRange) {
      throw ArgumentError('Description must be at least 10 characters long.');
    }
    description = description;
  }

  String get formattedDate {
    String data = 'Posted ${date.day}/${date.month}/${date.year}';
    if (lastUpdated != null) {
      data += '\nLast updated ${lastUpdated!.day}/${lastUpdated!.month}/${lastUpdated!.year}';
    }
    return data;
  }

  Text get displayDescription {
    return Text(
      content.length > 100 ? content.substring(0, 100) + '...' : content,
      style: const TextStyle(fontSize: 16.0),
    );
  }
}