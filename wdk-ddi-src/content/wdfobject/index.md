---
UID: NA:wdfobject
---

# Wdfobject.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfobject.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFOBJECTALLOCATECONTEXT function](nc-wdfobject-pfn_wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [PFN_WDFOBJECTCONTEXTGETOBJECT function](nc-wdfobject-pfn_wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [PFN_WDFOBJECTCREATE function](nc-wdfobject-pfn_wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [PFN_WDFOBJECTDELETE function](nc-wdfobject-pfn_wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [PFN_WDFOBJECTQUERY function](nc-wdfobject-pfn_wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
| [WDF_OBJECT_ATTRIBUTES_INIT function](nf-wdfobject-wdf_object_attributes_init.md) | The WDF_OBJECT_ATTRIBUTES_INIT function initializes a driver's WDF_OBJECT_ATTRIBUTES structure. |
| [WdfObjectAllocateContext function](nf-wdfobject-wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [WdfObjectContextGetObject function](nf-wdfobject-wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [WdfObjectCreate function](nf-wdfobject-wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [WdfObjectDelete function](nf-wdfobject-wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [WdfObjectDereferenceActual function](nf-wdfobject-wdfobjectdereferenceactual.md) | The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectGetTypedContextWorker function](nf-wdfobject-wdfobjectgettypedcontextworker.md) | The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead. |
| [WdfObjectQuery function](nf-wdfobject-wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
| [WdfObjectReferenceActual function](nf-wdfobject-wdfobjectreferenceactual.md) | The WdfObjectReferenceActual method increments the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_WDF_OBJECT_ATTRIBUTES structure](ns-wdfobject-_wdf_object_attributes.md) | The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object. |
| [_WDF_OBJECT_CONTEXT_TYPE_INFO structure](ns-wdfobject-_wdf_object_context_type_info.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_EXECUTION_LEVEL enumeration](ne-wdfobject-_wdf_execution_level.md) | The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object. |
| [_WDF_SYNCHRONIZATION_SCOPE enumeration](ne-wdfobject-_wdf_synchronization_scope.md) | The WDF_SYNCHRONIZATION_SCOPE enumeration type specifies how the framework will synchronize execution of an object's event callback functions. |

## Macros

| Title   | Description   |
| ---- |:---- |
| [WDF_GET_CONTEXT_TYPE_INFO macro](nf-wdfobject-wdf_get_context_type_info.md) | This macro is reserved for internal use only. |
| [WDF_TYPE_NAME_POINTER_TYPE macro](nf-wdfobject-wdf_type_name_pointer_type.md) | This macro is reserved for internal use only. |
| [WDF_TYPE_NAME_TO_TYPE_INFO macro](nf-wdfobject-wdf_type_name_to_type_info.md) | This macro is reserved for internal use only. |
