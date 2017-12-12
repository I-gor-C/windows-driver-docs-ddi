---
UID: NA:
---

# Wudfwdm.h header

## -description

This header is used by Windows kernel. For more information, see
- [Windows kernel](../_kernel/index.md)

Wudfwdm.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_OBJECT_ATTRIBUTES structure](ns-wudfwdm-_object_attributes.md) | The OBJECT_ATTRIBUTES structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects. |
| [_UNICODE_STRING structure](ns-wudfwdm-_unicode_string.md) | The UNICODE_STRING structure is used to define Unicode strings. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [ARGUMENT_PRESENT macro](nf-wudfwdm-argument_present.md) | The ARGUMENT_PRESENT macro takes an argument pointer and returns FALSE if the pointer is NULL. Otherwise, it returns TRUE. |
| [InitializeObjectAttributes macro](nf-wudfwdm-initializeobjectattributes.md) | The InitializeObjectAttributes macro initializes the opaque OBJECT_ATTRIBUTES structure, which specifies the properties of an object handle to routines that open handles. |
