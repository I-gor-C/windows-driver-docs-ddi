---
UID: NA:wdfobject
ms.assetid: 80bf670f-cd65-30cb-b7e7-be5741edc81e
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# wdfobject.h header



wdfobject.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_WDF_OBJECT_CONTEXT_CLEANUP](nc-wdfobject-evt_wdf_object_context_cleanup.md) | A driver's EvtCleanupCallback event callback function removes the driver's references on an object so that the object can be deleted. |
| [EVT_WDF_OBJECT_CONTEXT_DESTROY](nc-wdfobject-evt_wdf_object_context_destroy.md) | A driver's EvtDestroyCallback event callback function performs operations that are associated with the deletion of a framework object. |
| [WDF_GET_CONTEXT_TYPE_INFO](nf-wdfobject-wdf_get_context_type_info.md) | This macro is reserved for internal use only. |
| [WDF_OBJECT_ATTRIBUTES_INIT](nf-wdfobject-wdf_object_attributes_init.md) | The WDF_OBJECT_ATTRIBUTES_INIT function initializes a driver's WDF_OBJECT_ATTRIBUTES structure. |
| [WDF_TYPE_NAME_POINTER_TYPE](nf-wdfobject-wdf_type_name_pointer_type.md) | This macro is reserved for internal use only. |
| [WDF_TYPE_NAME_TO_TYPE_INFO](nf-wdfobject-wdf_type_name_to_type_info.md) | This macro is reserved for internal use only. |
| [WdfObjectAllocateContext](nf-wdfobject-wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [WdfObjectContextGetObject](nf-wdfobject-wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [WdfObjectCreate](nf-wdfobject-wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [WdfObjectDelete](nf-wdfobject-wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [WdfObjectDereferenceActual](nf-wdfobject-wdfobjectdereferenceactual.md) | The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectGetTypedContextWorker](nf-wdfobject-wdfobjectgettypedcontextworker.md) | The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead. |
| [WdfObjectQuery](nf-wdfobject-wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
| [WdfObjectReferenceActual](nf-wdfobject-wdfobjectreferenceactual.md) | The WdfObjectReferenceActual method increments the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |



## Structures
| Title | Description |
| ---- |:---- |
| [_WDF_OBJECT_ATTRIBUTES](ns-wdfobject-_wdf_object_attributes.md) | The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object. |
| [_WDF_OBJECT_CONTEXT_TYPE_INFO](ns-wdfobject-_wdf_object_context_type_info.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_WDF_EXECUTION_LEVEL](ne-wdfobject-_wdf_execution_level.md) | The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object. |
| [_WDF_SYNCHRONIZATION_SCOPE](ne-wdfobject-_wdf_synchronization_scope.md) | The WDF_SYNCHRONIZATION_SCOPE enumeration type specifies how the framework will synchronize execution of an object's event callback functions. |