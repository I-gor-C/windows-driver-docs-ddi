---
UID: NF.storport.StorPortGetSystemAddress
title: StorPortGetSystemAddress
author: windows-driver-content
description: The StorPortGetSystemAddress routine returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB).
old-location: storage\storportgetsystemaddress.htm
old-project: storage
ms.assetid: 28bb26bd-7259-4664-8092-6b9a917c1a91
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetSystemAddress
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Server 2003 with SP2.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetSystemAddress
req.alt-loc: storport.h
req.ddi-compliance: StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# StorPortGetSystemAddress function



## -description
<p>The <b>StorPortGetSystemAddress</b> routine returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB).</p>


## -syntax

````
ULONG StorPortGetSystemAddress(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _Out_ PVOID               *SystemAddress
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>Srb</i> [in]

<dd>
<p>A pointer to a <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> structure.</p>
</dd>

### -param <i>SystemAddress</i> [out]

<dd>
<p>A pointer to receive the virtual address of the data buffer.</p>
</dd>
</dl>

## -returns
<p>StorPortGetSystemAddress returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the system address was obtained successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>This status code is caused by one of the following conditions:
       </p>

<p>The SRB does not have an associated data buffer.</p>

<p>The pointer to receive the virtual address is <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The call was made at an invalid IRQL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The attempt to map the data buffer to system space failed.</p>

<p> </p>

## -remarks
<p>Starting in Windows 8, the <i>Srb</i> parameter may point to either <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> or <a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>. If the function identifier in the <b>Function</b> field of <i>Srb</i> is <b>SRB_FUNCTION_STORAGE_REQUEST_BLOCK</b>, the SRB is a <b>STORAGE_REQUEST_BLOCK</b> request structure.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available starting with Windows Server 2003 with SP2.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_storportirql">StorPortIrql</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
<dt>
<a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortGetSystemAddress routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
