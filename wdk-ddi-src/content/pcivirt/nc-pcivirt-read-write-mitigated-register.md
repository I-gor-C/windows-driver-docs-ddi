---
UID: NC.pcivirt.READ_WRITE_MITIGATED_REGISTER
title: READ_WRITE_MITIGATED_REGISTER
author: windows-driver-content
description: Reads or writes to mitigated address spaces.
old-location: pci\read_write_mitigated_registers.htm
old-project: PCI
ms.assetid: 7cd45484-0fee-4b8e-aa35-4142883c146e
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
req.alt-api: *PREAD_WRITE_MITIGATED_REGISTER
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

# READ_WRITE_MITIGATED_REGISTER callback



## -description
<p>Reads or writes to mitigated address spaces. </p>


## -prototype

````
READ_WRITE_MITIGATED_REGISTER ReadWriteMitigatedRegister;

NTSTATUS ReadWriteMitigatedRegister(
  _In_    PVOID     Context,
  _In_    USHORT    VfIndex,
  _In_    BOOLEAN   Read,
  _In_    USHORT    BarIndex,
  _In_    ULONGLONG Offset,
  _In_    ULONG     Length,
  _Inout_ PUCHAR    Data
)
{ ... }

typedef READ_WRITE_MITIGATED_REGISTER *PREAD_WRITE_MITIGATED_REGISTER;
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
<p>A zero-based index of the VF to which this read/write operation applies.</p>
</dd>

### -param <i>Read</i> [in]

<dd>
<p>
                    
                A boolean that indicates whether to perform a read or a write operation. TRUE indicates read, FALSE otherwise.</p>
</dd>

### -param <i>BarIndex</i> [in]

<dd>
<p>The BAR that maps the address space being mitigated.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The offset in number of bytes into the BAR at which this access begins.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>
                    
                The length in bytes of this read or write operation.</p>
</dd>

### -param <i>Data</i> [in, out]

<dd>
<p>A pointer to a buffer that contains the data to read or write.</p>
</dd>
</dl>

## -returns
<p>
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.</p>

## -remarks
<p>This callback function is implemented by the physical function (PF) driver. It is invoked  when the system wants to read or write from a mitigable register. </p>

<p>The PF driver registers its implementation by setting the <b>ReadWriteMitigatedRegister</b> member of the <a href="buses._mitigable_device_interface">MITIGABLE_DEVICE_INTERFACE</a>, configuring a <a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure, and calling <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.</p>

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