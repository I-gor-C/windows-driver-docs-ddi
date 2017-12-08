# Wdfobject.h header


This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfobject.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WDF_OBJECT_ATTRIBUTES_INIT function](nf-wdfobject-wdf-object-attributes-init.md) | The WDF_OBJECT_ATTRIBUTES_INIT function initializes a driver's WDF_OBJECT_ATTRIBUTES structure. |
| [WdfObjectAllocateContext function](nf-wdfobject-wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [WdfObjectContextGetObject function](nf-wdfobject-wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [WdfObjectCreate function](nf-wdfobject-wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [WdfObjectDelete function](nf-wdfobject-wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [WdfObjectDereferenceActual function](nf-wdfobject-wdfobjectdereferenceactual.md) | The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectGetTypedContextWorker function](nf-wdfobject-wdfobjectgettypedcontextworker.md) | The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead. |
| [WdfObjectQuery function](nf-wdfobject-wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
| [WdfObjectReferenceActual function](nf-wdfobject-wdfobjectreferenceactual.md) | The WdfObjectReferenceActual method increments the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_WDF_OBJECT_CONTEXT_CLEANUP callback](nc-wdfobject-evt-wdf-object-context-cleanup.md) | A driver's EvtCleanupCallback event callback function removes the driver's references on an object so that the object can be deleted. |
| [EVT_WDF_OBJECT_CONTEXT_DESTROY callback](nc-wdfobject-evt-wdf-object-context-destroy.md) | A driver's EvtDestroyCallback event callback function performs operations that are associated with the deletion of a framework object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [WDF_OBJECT_ATTRIBUTES structure](ns-wdfobject--wdf-object-attributes.md) | The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object. |
| [WDF_OBJECT_CONTEXT_TYPE_INFO structure](ns-wdfobject--wdf-object-context-type-info.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |
| [WDF_OBJECT_CONTEXT_TYPE_INFO structure](ns-wdfobject--wdf-object-context-type-info~r1.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDF_EXECUTION_LEVEL enumeration](ne-wdfobject--wdf-execution-level.md) | The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object. |
| [WDF_SYNCHRONIZATION_SCOPE enumeration](ne-wdfobject--wdf-synchronization-scope.md) | The WDF_SYNCHRONIZATION_SCOPE enumeration type specifies how the framework will synchronize execution of an object's event callback functions. |
