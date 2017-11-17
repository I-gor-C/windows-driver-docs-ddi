# Declarations in the wdfobject header
This header Wdfobject contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfObjectAllocateContext function](nf-wdfobject-wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [WDF_OBJECT_ATTRIBUTES_INIT function](nf-wdfobject-wdf-object-attributes-init.md) | The WDF_OBJECT_ATTRIBUTES_INIT function initializes a driver's WDF_OBJECT_ATTRIBUTES structure. |
| [WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE function](nf-wdfobject-wdf-object-attributes-set-context-type.md) | TBD |
| [WDF_DECLARE_CONTEXT_TYPE function](nf-wdfobject-wdf-declare-context-type.md) | TBD |
| [WDF_DECLARE_CASTING_FUNCTION function](nf-wdfobject-wdf-declare-casting-function.md) | TBD |
| [WdfObjectAddCustomType function](nf-wdfobject-wdfobjectaddcustomtype.md) | TBD |
| [WDF_CUSTOM_TYPE_CONTEXT_NAME function](nf-wdfobject-wdf-custom-type-context-name.md) | TBD |
| [WdfObjectGetTypedContext function](nf-wdfobject-wdfobjectgettypedcontext.md) | TBD |
| [WDF_TYPE_NAME_POINTER_TYPE function](nf-wdfobject-wdf-type-name-pointer-type.md) | TBD |
| [WdfObjectContextGetObject function](nf-wdfobject-wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [WdfObjectGetTypedContextWorker function](nf-wdfobject-wdfobjectgettypedcontextworker.md) | The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead. |
| [WdfObjectDereferenceWithTag function](nf-wdfobject-wdfobjectdereferencewithtag.md) | TBD |
| [WdfObjectReferenceActual function](nf-wdfobject-wdfobjectreferenceactual.md) | The WdfObjectReferenceActual method increments the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WDF_GET_CUSTOM_TYPE_FUNCTION_NAME function](nf-wdfobject-wdf-get-custom-type-function-name.md) | TBD |
| [WDF_TYPE_NAME_TO_TYPE_INFO function](nf-wdfobject-wdf-type-name-to-type-info.md) | TBD |
| [WdfObjectReferenceWithTag function](nf-wdfobject-wdfobjectreferencewithtag.md) | TBD |
| [WDF_TYPE_NAME_TO_EXTERNAL_INIT function](nf-wdfobject-wdf-type-name-to-external-init.md) | TBD |
| [WDF_DECLARE_SHARED_CONTEXT_TYPE_WITH_NAME function](nf-wdfobject-wdf-declare-shared-context-type-with-name.md) | TBD |
| [WdfObjectDereference function](nf-wdfobject-wdfobjectdereference.md) | TBD |
| [WdfObjectIsCustomType function](nf-wdfobject-wdfobjectiscustomtype.md) | TBD |
| [WDF_DECLARE_CONTEXT_TYPE_WITH_NAME function](nf-wdfobject-wdf-declare-context-type-with-name.md) | TBD |
| [WDF_DECLARE_CUSTOM_TYPE function](nf-wdfobject-wdf-declare-custom-type.md) | TBD |
| [WDF_ADD_CUSTOM_TYPE_FUNCTION_NAME function](nf-wdfobject-wdf-add-custom-type-function-name.md) | TBD |
| [WdfObjectReference function](nf-wdfobject-wdfobjectreference.md) | TBD |
| [WdfObjectAddCustomTypeWithData function](nf-wdfobject-wdfobjectaddcustomtypewithdata.md) | TBD |
| [WdfObjectCreate function](nf-wdfobject-wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [WdfObjectDereferenceActual function](nf-wdfobject-wdfobjectdereferenceactual.md) | The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectGetCustomTypeData function](nf-wdfobject-wdfobjectgetcustomtypedata.md) | TBD |
| [WdfObjectDelete function](nf-wdfobject-wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [WdfObjectQuery function](nf-wdfobject-wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
| [WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE function](nf-wdfobject-wdf-object-attributes-init-context-type.md) | TBD |
| [WDF_GET_CONTEXT_TYPE_INFO function](nf-wdfobject-wdf-get-context-type-info.md) | TBD |
| [WDF_TYPE_NAME_TO_EXTERNAL_INIT_FUNCTION function](nf-wdfobject-wdf-type-name-to-external-init-function.md) | TBD |
| [WDF_DECLARE_TYPE_AND_GLOBALS function](nf-wdfobject-wdf-declare-type-and-globals.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_OBJECT_CONTEXT_CLEANUP callback](nc-wdfobject-evt-wdf-object-context-cleanup.md) | A driver's EvtCleanupCallback event callback function removes the driver's references on an object so that the object can be deleted. |
| [PFN_WDFOBJECTGETTYPEDCONTEXTWORKER callback function](nc-wdfobject-pfn-wdfobjectgettypedcontextworker.md) | TBD |
| [PFN_WDFOBJECTDELETE callback function](nc-wdfobject-pfn-wdfobjectdelete.md) | TBD |
| [PFN_WDFOBJECTREFERENCEACTUAL callback function](nc-wdfobject-pfn-wdfobjectreferenceactual.md) | TBD |
| [PFN_GET_UNIQUE_CONTEXT_TYPE callback function](nc-wdfobject-pfn-get-unique-context-type.md) | TBD |
| [PFN_WDFOBJECTCONTEXTGETOBJECT callback function](nc-wdfobject-pfn-wdfobjectcontextgetobject.md) | TBD |
| [PFN_WDFOBJECTALLOCATECONTEXT callback function](nc-wdfobject-pfn-wdfobjectallocatecontext.md) | TBD |
| [PFN_WDFOBJECTCREATE callback function](nc-wdfobject-pfn-wdfobjectcreate.md) | TBD |
| [EVT_WDF_OBJECT_CONTEXT_DESTROY callback](nc-wdfobject-evt-wdf-object-context-destroy.md) | A driver's EvtDestroyCallback event callback function performs operations that are associated with the deletion of a framework object. |
| [PFN_WDFOBJECTDEREFERENCEACTUAL callback function](nc-wdfobject-pfn-wdfobjectdereferenceactual.md) | TBD |
| [PFN_WDFOBJECTQUERY callback function](nc-wdfobject-pfn-wdfobjectquery.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_SYNCHRONIZATION_SCOPE enumeration](ne-wdfobject--wdf-synchronization-scope.md) | The WDF_SYNCHRONIZATION_SCOPE enumeration type specifies how the framework will synchronize execution of an object's event callback functions. |
| [WDF_EXECUTION_LEVEL enumeration](ne-wdfobject--wdf-execution-level.md) | The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_OBJECT_CONTEXT_TYPE_INFO structure](ns-wdfobject--wdf-object-context-type-info~r1.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |
| [WDF_CUSTOM_TYPE_CONTEXT structure](ns-wdfobject--wdf-custom-type-context.md) | TBD |
| [WDF_OBJECT_CONTEXT_TYPE_INFO structure](ns-wdfobject--wdf-object-context-type-info.md) | TBD |
| [WDF_OBJECT_ATTRIBUTES structure](ns-wdfobject--wdf-object-attributes.md) | The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object. |

This header is used in these topics:

- [wdf](..content/_wdf)
