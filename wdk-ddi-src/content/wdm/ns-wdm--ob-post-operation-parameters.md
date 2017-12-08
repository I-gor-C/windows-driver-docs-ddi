---
UID: NS.wdm._OB_POST_OPERATION_PARAMETERS
title: OB_POST_OPERATION_PARAMETERS
author: windows-driver-content
description: The OB_POST_OPERATION_PARAMETERS union describes the operation-specific parameters for an ObjectPostCallback routine.
old-location: kernel\ob_post_operation_parameters.htm
old-project: kernel
ms.assetid: cd0551fc-c276-45c3-a560-bded300a4535
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: OB_POST_OPERATION_PARAMETERS, OB_POST_OPERATION_PARAMETERS, *POB_POST_OPERATION_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Server 2008 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OB_POST_OPERATION_PARAMETERS
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# OB_POST_OPERATION_PARAMETERS structure



## -description
<p>The <b>OB_POST_OPERATION_PARAMETERS</b> union describes the operation-specific parameters for an <a href="kernel.objectpostcallback">ObjectPostCallback</a> routine.</p>


## -syntax

````
typedef union _OB_POST_OPERATION_PARAMETERS {
  OB_POST_CREATE_HANDLE_INFORMATION    CreateHandleInformation;
  OB_POST_DUPLICATE_HANDLE_INFORMATION DuplicateHandleInformation;
} OB_POST_OPERATION_PARAMETERS, *POB_POST_OPERATION_PARAMETERS;
````


## -struct-fields
<dl>

### -field CreateHandleInformation

<dd>
<p>An <a href="..\wdm\ns-wdm--ob-post-create-handle-information.md">OB_POST_CREATE_HANDLE_INFORMATION</a> structure that contains information that is specific to a handle that is being opened.</p>
</dd>

### -field DuplicateHandleInformation

<dd>
<p>An <a href="..\wdm\ns-wdm--ob-post-duplicate-handle-information.md">OB_POST_DUPLICATE_HANDLE_INFORMATION</a> structure that contains information that is specific to a handle that is being duplicated.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Server 2008 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--ob-post-create-handle-information.md">OB_POST_CREATE_HANDLE_INFORMATION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--ob-post-duplicate-handle-information.md">OB_POST_DUPLICATE_HANDLE_INFORMATION</a>
</dt>
<dt>
<a href="kernel.objectpostcallback">ObjectPostCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20OB_POST_OPERATION_PARAMETERS union%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
