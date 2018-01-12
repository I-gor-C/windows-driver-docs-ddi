---
UID: NC:wdfcommonbuffer.PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS
title: PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS function
author: windows-driver-content
description: The WdfCommonBufferGetAlignedVirtualAddress method returns the virtual address that is associated with a specified common buffer.
old-location: wdf\wdfcommonbuffergetalignedvirtualaddress.htm
old-project: wdf
ms.assetid: 6874a1bc-e16e-4052-85a4-dba617a69ccd
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcommonbuffer.h
req.include-header: WdfCommonBuffer.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfCommonBufferGetAlignedVirtualAddress
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
req.irql: <= DISPATCH_LEVEL
req.typenames: *PWDF_CHILD_RETRIEVE_INFO, WDF_CHILD_RETRIEVE_INFO
req.product: Windows 10 or later.
---

# PFN_WDFCOMMONBUFFERGETALIGNEDVIRTUALADDRESS function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfCommonBufferGetAlignedVirtualAddress</b> method returns the virtual address that is associated with a specified common buffer. 



## -syntax

````
PVOID WdfCommonBufferGetAlignedVirtualAddress(
  _In_ WDFCOMMONBUFFER CommonBuffer
);
````


## -parameters

### -param CommonBuffer [in]

A handle to a common buffer object that the driver obtained by a previous call to <a href="..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffercreate.md">WdfCommonBufferCreate</a>.  


## -returns
<b>WdfCommonBufferGetAlignedVirtualAddress</b> returns the virtual address of the buffer that is associated with the common buffer that the <i>CommonBuffer</i> parameter specifies.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
If the driver called <a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetalignmentrequirement.md">WdfDeviceSetAlignmentRequirement</a> to set a buffer alignment requirement, the framework aligns the common buffer according to that alignment requirement.

For more information about common buffers, see <a href="https://msdn.microsoft.com/81a56f62-917e-4798-b2cc-6469c802fab8">Using Common Buffers</a>


For a code example that uses <b>WdfCommonBufferGetAlignedVirtualAddress</b>, see <a href="..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffercreate.md">WdfCommonBufferCreate</a>.


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
<dt>Wdfcommonbuffer.h (include WdfCommonBuffer.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffercreate.md">WdfCommonBufferCreate</a>
</dt>
<dt>
<a href="..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffergetalignedlogicaladdress.md">WdfCommonBufferGetAlignedLogicalAddress</a>
</dt>
<dt>
<a href="..\wdfdevice\nf-wdfdevice-wdfdevicesetalignmentrequirement.md">WdfDeviceSetAlignmentRequirement</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCommonBufferGetAlignedVirtualAddress method%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

