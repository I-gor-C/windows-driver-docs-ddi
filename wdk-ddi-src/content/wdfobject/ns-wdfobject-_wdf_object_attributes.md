---
UID: NS.WDFOBJECT._WDF_OBJECT_ATTRIBUTES
title: _WDF_OBJECT_ATTRIBUTES
author: windows-driver-content
description: The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object.
old-location: wdf\wdf_object_attributes.htm
old-project: wdf
ms.assetid: 3331c2d8-3100-410d-9c75-33a3b55d5a49
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _WDF_OBJECT_ATTRIBUTES, WDF_OBJECT_ATTRIBUTES, *PWDF_OBJECT_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfobject.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_OBJECT_ATTRIBUTES
req.alt-loc: wdfobject.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _WDF_OBJECT_ATTRIBUTES structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object.


## -syntax

````
typedef struct _WDF_OBJECT_ATTRIBUTES {
  ULONG                          Size;
  PFN_WDF_OBJECT_CONTEXT_CLEANUP EvtCleanupCallback;
  PFN_WDF_OBJECT_CONTEXT_DESTROY EvtDestroyCallback;
  WDF_EXECUTION_LEVEL            ExecutionLevel;
  WDF_SYNCHRONIZATION_SCOPE      SynchronizationScope;
  WDFOBJECT                      ParentObject;
  size_t                         ContextSizeOverride;
  PCWDF_OBJECT_CONTEXT_TYPE_INFO ContextTypeInfo;
} WDF_OBJECT_ATTRIBUTES, *PWDF_OBJECT_ATTRIBUTES;
````


## -struct-fields

### -field Size

The size, in bytes, of this structure.

### -field EvtCleanupCallback

A pointer to the driver's <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> callback function, or <b>NULL</b>.

### -field EvtDestroyCallback

A pointer to the driver's <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_destroy.md">EvtDestroyCallback</a> callback function, or <b>NULL</b>.

### -field ExecutionLevel

A <a href="wdf.wdf_execution_level">WDF_EXECUTION_LEVEL</a>-typed value that specifies the maximum IRQL at which the framework will call the object's event callback functions. For a list of framework objects for which the driver can specify an <b>ExecutionLevel</b> value, see <a href="wdf.wdf_execution_level">WDF_EXECUTION_LEVEL</a>.

### -field SynchronizationScope

A <a href="wdf.wdf_synchronization_scope">WDF_SYNCHRONIZATION_SCOPE</a>-typed value that specifies how the framework will synchronize execution of the object's event callback functions. For a list of framework objects for which the driver can specify a <b>SynchronizationScope</b> value, see <a href="wdf.wdf_synchronization_scope">WDF_SYNCHRONIZATION_SCOPE</a>.

### -field ParentObject

A handle to the object's parent object, or <b>NULL</b> if the object does not have a driver-specified parent. 
See <a href="wdf.summary_of_framework_objects">Summary of Framework Objects</a> for a table that shows the objects that allow a driver-specified parent. The table also shows the default parent of each object. 

### -field ContextSizeOverride

If not zero, this value overrides the <b>ContextSize</b> member of the <a href="wdf.wdf_object_context_type_info">WDF_OBJECT_CONTEXT_TYPE_INFO</a> structure that the <b>ContextTypeInfo</b> member references. This value is optional and can be zero. If the value is not zero, it must specify a size, in bytes, that is larger than the value that is specified for the <b>ContextSize</b> member of the WDF_OBJECT_CONTEXT_TYPE_INFO structure. For more information, see the following Remarks section.

### -field ContextTypeInfo

A pointer to a <a href="wdf.wdf_object_context_type_info">WDF_OBJECT_CONTEXT_TYPE_INFO</a> structure. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552405">WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE</a> macro sets this pointer.

## -remarks
The WDF_OBJECT_ATTRIBUTES structure is used as an input argument to several methods that create framework objects.

To initialize a WDF_OBJECT_ATTRIBUTES structure, the driver must call <a href="wdf.wdf_object_attributes_init">WDF_OBJECT_ATTRIBUTES_INIT</a>. 

Additionally, if you are defining object-specific context information for an object, you must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552405">WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE</a> macro. 

Alternatively, you can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a> macro instead of the WDF_OBJECT_ATTRIBUTES_INIT and WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE macros.

For more information about using these macros, see <a href="wdf.framework_object_context_space">Framework Object Context Space</a>.

Use the <b>ContextSizeOverride</b> member of WDF_OBJECT_ATTRIBUTES if you want to create <a href="wdf.framework_object_context_space">object context space</a> that has a variable length. For example, you might define a context space structure that contains an array, as follows:

When your driver creates an object that uses the context space structure, it can use the <b>ContextSizeOverride</b> member to specify the context size that is needed for each individual object. For example, your driver might calculate the number of bytes that are needed in the array from the preceding example and then use <b>ContextSizeOverride</b> to specify the extra bytes, as follows:

The driver can then create an object with a customized context size.

## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfobject.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfobjectallocatecontext">WdfObjectAllocateContext</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes_init">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552404">WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552405">WDF_OBJECT_ATTRIBUTES_SET_CONTEXT_TYPE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_OBJECT_ATTRIBUTES structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
