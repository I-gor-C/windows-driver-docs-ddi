---
UID: NF.oprghdlr.RegisterOpRegionHandler
title: RegisterOpRegionHandler
author: windows-driver-content
description: The RegisterOpRegionHandler routine registers an operation region handler with the ACPI driver.
old-location: acpi\registeropregionhandler.htm
old-project: acpi
ms.assetid: 5795a1d1-0e13-4f9f-b2f2-37bbd71bde7a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RegisterOpRegionHandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: oprghdlr.h
req.include-header: Oprghdlr.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RegisterOpRegionHandler
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
req.iface: 
---

# RegisterOpRegionHandler function



## -description
<p>The <b>RegisterOpRegionHandler</b> routine registers an operation region handler with the <a href="https://msdn.microsoft.com/38ca54e0-defe-48b2-ab00-a5f688c2eb01">ACPI driver</a>.</p>


## -syntax

````
NTSTATUS RegisterOpRegionHandler(
  _In_  PDEVICE_OBJECT          DeviceObject,
  _In_  ULONG                   AccessType,
  _In_  ULONG                   RegionSpace,
  _In_  PACPI_OP_REGION_HANDLER Handler,
  _In_  PVOID                   Context,
  _In_  ULONG                   Flags,
  _Out_ PVOID                   *OperationRegionObject
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>Pointer to the physical device object (<a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>) that represents the ACPI device that defines the operation region.</p>
</dd>

### -param AccessType [in]

<dd>
<p>Specifies ACPI_OPREGION_ACCESS_AS_COOKED.</p>
</dd>

### -param RegionSpace [in]

<dd>
<p>Specifies one of the following types of region space.</p>
<table>
<tr>
<th>Region Space Identifier</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_MEMORY</p>
</td>
<td>
<p>System memory</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_IO</p>
</td>
<td>
<p>I/O space</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_PCI_CONFIG</p>
</td>
<td>
<p>PCI configuration</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_EC</p>
</td>
<td>
<p>Embedded controller</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_SMB</p>
</td>
<td>
<p>System Management Bus</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_CMOS_CONFIG</p>
</td>
<td>
<p>CMOS configuration</p>
</td>
</tr>
<tr>
<td>
<p>ACPI_OPREGION_REGION_SPACE_PCIBARTARGET</p>
</td>
<td>
<p>PCI Base Address Register</p>
</td>
</tr>
<tr>
<td>
<p>Vendor-defined value from 0x80 to 0xFF</p>
</td>
<td>
<p>Vendor-defined</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Handler [in]

<dd>
<p>Pointer to the <a href="..\oprghdlr\nc-oprghdlr-acpi-op-region-handler.md">ACPI_OP_REGION_HANDLER</a>-typed operation region handler (supplied by an ACPI device function driver).</p>
</dd>

### -param Context [in]

<dd>
<p>Pointer to a device-specific operation region context (supplied by an ACPI device function driver).</p>
</dd>

### -param Flags [in]

<dd>
<p>Reserved for internal use.</p>
</dd>

### -param OperationRegionObject [out]

<dd>
<p>Pointer to caller-allocated buffer that, on output, contains a pointer to the operation region object that the ACPI driver creates for the operation region.</p>
</dd>
</dl>

## -returns
<p>Returns one of the following status values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operating region handler was successfully registered.</p><dl>
<dt><b>STATUS_ACPI_INVALID_DATA</b></dt>
</dl><p>The specified information is not valid.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The routine could not allocate the necessary system resources.</p><dl>
<dt><b>STATUS_Xxx</b></dt>
</dl><p>An internal error occurred.</p>

<p> </p>

## -remarks
<p>The operation region context specified by <i>Context</i> is device-specific and is only used by the function driver. Typically, the context is the device extension for the functional device object (<a href="wdkgloss.f#wdkgloss.fdo#wdkgloss.fdo"><i>FDO</i></a>). The ACPI driver passes this context back to the function driver when it calls the operation region handler. The operation region object is only used by a function driver to uniquely identify the operation region when it deregisters the operation region handler.</p>

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
<a href="..\oprghdlr\nf-oprghdlr-deregisteropregionhandler.md">DeRegisterOpRegionHandler</a>
</dt>
<dt>
<a href="..\oprghdlr\nc-oprghdlr-acpi-op-region-handler.md">ACPI_OP_REGION_HANDLER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [acpi\acpi]:%20RegisterOpRegionHandler routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
