---
UID: NF.oprghdlr.DeRegisterOpRegionHandler
title: DeRegisterOpRegionHandler
author: windows-driver-content
description: The DeRegisterOpRegionHandler routine deregisters an operation region handler with the ACPI driver.
old-location: acpi\deregisteropregionhandler.htm
ms.assetid: b50a63cd-69eb-46a8-9d0b-660795c7047f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: acpi
req.header: oprghdlr.h
req.include-header: Oprghdlr.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DeRegisterOpRegionHandler
req.alt-loc: Oprghdlr.lib,Oprghdlr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Oprghdlr.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DeRegisterOpRegionHandler
req.iface: 
---

# DeRegisterOpRegionHandler function



## -description
<p>The <b>DeRegisterOpRegionHandler</b> routine deregisters an operation region handler with the <a href="https://msdn.microsoft.com/38ca54e0-defe-48b2-ab00-a5f688c2eb01">ACPI driver</a>.</p>


## -syntax

````
NTSTATUS DeRegisterOpRegionHandler(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PVOID          OperationRegionObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the physical device object (PDO) that represents the ACPI device that defines the operation region.</p>
</dd>

### -param <i>OperationRegionObject</i> [in]

<dd>
<p>Specifies the operation region object returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff536158">RegisterOpRegionHandler</a> for the operation region handler.</p>
</dd>
</dl>

## -returns
<p>Returns one of the following status values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operating region handler was successfully registered.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The routine could not allocate the necessary system resources.</p><dl>
<dt><b>STATUS_Xxx</b></dt>
</dl><p>An internal error occurred.</p>

<p> </p>

## -remarks
<p>This routine is used in combination with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536158">RegisterOpRegionHandler</a>. To deregister an operation region handler, the caller must specify the operation region object returned by <b>RegisterOpRegionHandler</b> when it registered the operation region handler.</p>

<p>For more information about operation regions, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/supporting-an-operation-region">Supporting an Operation Region</a>. </p>

<p>This routine is used in combination with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536158">RegisterOpRegionHandler</a>. To deregister an operation region handler, the caller must specify the operation region object returned by <b>RegisterOpRegionHandler</b> when it registered the operation region handler.</p>

<p>For more information about operation regions, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/acpi/supporting-an-operation-region">Supporting an Operation Region</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Oprghdlr.h (include Oprghdlr.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Oprghdlr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536158">RegisterOpRegionHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536153">ACPI_OP_REGION_HANDLER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [acpi\acpi]:%20DeRegisterOpRegionHandler routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
