---
UID: NF.wudfddi_hwaccess.READ_REGISTER_BUFFER_USHORT
title: READ_REGISTER_BUFFER_USHORT
author: windows-driver-content
description: The READ_REGISTER_BUFFER_USHORT function reads a number of USHORT values from the specified register address into a buffer.
old-location: wdf\read_register_buffer_ushort.htm
old-project: wdf
ms.assetid: 0CA07C11-7E46-4225-AC61-5183C322604E
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: READ_REGISTER_BUFFER_USHORT
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
req.alt-api: READ_REGISTER_BUFFER_USHORT
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

# READ_REGISTER_BUFFER_USHORT function



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>READ_REGISTER_BUFFER_USHORT</b> function reads a number of USHORT values from the specified register address into a buffer.</p>


## -syntax

````
void READ_REGISTER_BUFFER_USHORT(
  _In_  IWDFDevice3 *pDevice,
  _In_  PUSHORT     Register,
  _Out_ PUSHORT     Buffer,
  _In_  ULONG       Count 
);
````


## -parameters
<dl>

### -param pDevice [in]

<dd>
<p>Specifies a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfdevice3.md">IWDFDevice3</a> interface for the device object of the device to access.</p>
</dd>

### -param Register [in]

<dd>
<p>A pointer to the register, which must be a mapped range in memory space.</p>
</dd>

### -param Buffer [out]

<dd>
<p>A pointer to a buffer into which an array of USHORT values is read.</p>
</dd>

### -param Count  [in]

<dd>
<p>Specifies the number of USHORT values to be read into the buffer.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
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