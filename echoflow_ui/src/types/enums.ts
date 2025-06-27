export const UserRole = {
  ADMIN: "admin",
  ORGANIZER: "organizer",
  ANALYST: "analyst",
  REPORTER: "reporter",
  PERSONAL: "personal",
  STUDENT: "student",
  MODERATOR: "moderator",
} as const;

export type UserRole = (typeof UserRole)[keyof typeof UserRole];

// Optional utility
export function isUserRole(value: any): value is UserRole {
  return Object.values(UserRole).includes(value);
}