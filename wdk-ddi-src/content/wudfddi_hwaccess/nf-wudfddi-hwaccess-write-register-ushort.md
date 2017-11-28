---
UID: NF.wudfddi_hwaccess.WRITE_REGISTER_USHORT
title: WRITE_REGISTER_USHORT
author: windows-driver-content
description: The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address.
old-location: wdf\write_register_ushort.htm
old-project: wdf
ms.assetid: F41E7DD6-336C-477D-87AD-0151A523DD0A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WRITE_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi_hwaccess.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WRITE_REGISTER_USHORT
req.alt-loc: Wudfddi_hwaccess.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WRITE_REGISTER_USHORT function



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>WRITE_REGISTER_USHORT</b> routine writes a USHORT value to the specified address.</p>


## -syntax

````
void WRITE_REGISTER_USHORT(
  _In_ IWDFDevice3 *pDevice,
  _In_ PUSHORT     Register,
  _In_ ULONG       Value
);
````


## -parameters
<dl>

### -param <i>pDevice</i> [in]

<dd>
<p>Specifies a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451197">IWDFDevice3</a> interface for the device object of the device to access.</p>
</dd>

### -param <i>Register</i> [in]

<dd>
<p>A pointer to the register address, which must be a mapped range in memory space.</p>
</dd>

### -param <i>Value</i> [in]

<dd>
<p>Specifies a USHORT value to write to the register.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>For more information, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

<p>For more information, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_hwaccess.h</dt>
</dl>
</td>
</tr>
</table>