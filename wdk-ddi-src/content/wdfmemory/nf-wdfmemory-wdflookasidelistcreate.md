---
UID: NF.wdfmemory.WdfLookasideListCreate
title: WdfLookasideListCreate function
author: windows-driver-content
description: The WdfLookasideListCreate method creates a lookaside-list object, from which the driver can obtain memory objects.
old-location: wdf\wdflookasidelistcreate.htm
old-project: wdf
ms.assetid: 37fc86b0-de8c-469b-94bb-ad482b9c7202
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfLookasideListCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfLookasideListCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# WdfLookasideListCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfLookasideListCreate</b> method creates a lookaside-list object, from which the driver can obtain memory objects. 



## -syntax

````
NTSTATUS WdfLookasideListCreate(
  _In_opt_ PWDF_OBJECT_ATTRIBUTES LookasideAttributes,
  _In_     size_t                 BufferSize,
  _In_     POOL_TYPE              PoolType,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES MemoryAttributes,
  _In_opt_ ULONG                  PoolTag,
  _Out_    WDFLOOKASIDE           *Lookaside
);
````


## -parameters

### -param LookasideAttributes [in, optional]

A pointer to a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains object attributes for the new lookaside-list object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


### -param BufferSize [in]

The nonzero size, in bytes, of the buffer that the framework will allocate for each memory object. 


### -param PoolType [in]

A <a href="kernel.pool_type">POOL_TYPE</a>-typed value that specifies the type of memory to be allocated. 


### -param MemoryAttributes [in, optional]

A pointer to a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains object attributes for each memory object that the driver obtains from the lookaside list. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


### -param PoolTag [in, optional]

A driver-defined pool tag for each memory object's buffer. Debuggers display this tag. Drivers typically specify a character string of up to four characters, delimited by single quotation marks, in reverse order (for example, 'dcba'). The ASCII value of each character in the tag must be between 0 and 127. Debugging your driver is easier if each pool tag is unique. 

If <i>PoolTag</i> is zero, the framework provides a default pool tag that uses the first four characters of your driver's kernel-mode service name. If the service name begins with "WDF" (the name is not case sensitive and does not include the quotation marks), the next four characters are used. If fewer than four characters are available, "FxDr" is used.

For KMDF versions 1.5 and later, your driver can use the <b>DriverPoolTag</b> member of the <a href="wdf.wdf_driver_config">WDF_DRIVER_CONFIG</a> structure to specify a default pool tag.


### -param Lookaside [out]

A pointer to a location that receives a handle to the new lookaside-list object.


## -returns
<b>WdfLookasideListCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was detected.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There was insufficient memory.

 

For a list of other return values that the <b>WdfLookasideListCreate</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


## -remarks
After your driver calls <b>WdfLookasideListCreate</b> to create a lookaside-list object, the driver can call <a href="wdf.wdfmemorycreatefromlookaside">WdfMemoryCreateFromLookaside</a> to obtain a buffer from the lookaside list. 

By default, the new lookaside-list object's parent is the framework driver object that the <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> method creates. You can use the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the lookaside-list object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the lookaside-list object when it has finished using the object; otherwise, the lookaside-list object will remain until the I/O manager unloads your driver. 

If your driver supplies a WDF_OBJECT_ATTRIBUTES structure for both the <i>LookasideAttributes</i> and the <i>MemoryAttributes</i> parameters, and if both structures specify a device object as the parent object, the device object handles must be the same. 

For more information about framework memory objects and lookaside lists, see <a href="wdf.using_memory_buffers">Using Memory Buffers</a>.

If your driver specifies <b>PagedPool</b> for the <i>PoolType</i> parameter, the <b>WdfLookasideListCreate</b> method must be called at IRQL &lt;= APC_LEVEL. Otherwise, the method can be called at IRQL &lt;= DISPATCH_LEVEL.

For a code example that uses <b>WdfLookasideListCreate</b>, see <a href="wdf.wdfmemorycreatefromlookaside">WdfMemoryCreateFromLookaside</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
Header

</th>
<td width="70%">
<dl>
<dt>Wdfmemory.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks section.

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfmemorycreatefromlookaside">WdfMemoryCreateFromLookaside</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfLookasideListCreate method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

