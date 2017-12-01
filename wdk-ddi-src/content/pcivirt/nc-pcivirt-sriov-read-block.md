---
UID: NC.pcivirt.SRIOV_READ_BLOCK
title: SRIOV_READ_BLOCK
author: windows-driver-content
description: Reads data from the specified configuration block of a PCI Express SR-IOV Virtual Function (VF).
old-location: pci\sriov_read_block.htm
old-project: PCI
ms.assetid: af0d3465-2854-47d9-a6a4-06f510229a59
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PSRIOV_READ_BLOCK
req.alt-loc: Pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# SRIOV_READ_BLOCK callback



## -description
<p>Reads data from the specified configuration block of a PCI Express SR-IOV Virtual Function (VF).</p>


## -prototype

````
SRIOV_READ_BLOCK SriovReadBlock;

NTSTATUS SriovReadBlock(
  _In_  PVOID  Context,
  _In_  USHORT VfIndex,
  _In_  ULONG  BlockId,
  _Out_ PVOID  Buffer,
  _In_  ULONG  Length
)
{ ... }

typedef SRIOV_READ_BLOCK *PSRIOV_READ_BLOCK;
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to a driver-defined context.
                    
                </p>
</dd>

### -param <i>VfIndex</i> [in]

<dd>
<p>A zero-based index of the VF to which this read operation applies.</p>
</dd>

### -param <i>BlockId</i> [in]

<dd>
<p>A number identifying the block to be read.  This is defined by the provider of the PF driver.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a buffer that receives the data read from the VF's  configuration space.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length in bytes of this read operation.  Must not be greater than VPCI_MAX_READ_WRITE_BLOCK_SIZE defined in Pcivirt.h.</p>
</dd>
</dl>

## -returns
<p>
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.</p>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to read a configuration block for one of its VFs.</p>

<p>The PF driver registers its implementation by setting the <b>ReadVfConfigBlock</b> member of the <a href="buses._sriov_device_interface_standard">SRIOV_DEVICE_INTERFACE_STANDARD</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pcivirt.h</dt>
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