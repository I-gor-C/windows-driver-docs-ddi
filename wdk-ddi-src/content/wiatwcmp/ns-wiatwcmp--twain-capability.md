---
UID: NS.wiatwcmp._TWAIN_CAPABILITY
title: TWAIN_CAPABILITY
author: windows-driver-content
description: The TWAIN_CAPABILITY structure holds information used when a TWAIN-compatible application communicates with a WIA driver.
old-location: image\twain_capability.htm
old-project: image
ms.assetid: 79a2155d-eb06-4095-9fe6-b95d93e46211
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TWAIN_CAPABILITY, TWAIN_CAPABILITY, *PTWAIN_CAPABILITY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiatwcmp.h
req.include-header: Wiatwcmp.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TWAIN_CAPABILITY
req.alt-loc: wiatwcmp.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# TWAIN_CAPABILITY structure



## -description
<p>The TWAIN_CAPABILITY structure holds information used when a TWAIN-compatible application communicates with a WIA driver.</p>


## -syntax

````
typedef struct _TWAIN_CAPABILITY {
  LONG lSize;
  LONG lMSG;
  LONG lCapID;
  LONG lConType;
  LONG lRC;
  LONG lCC;
  LONG lDataSize;
  BYTE Data[1];
} TWAIN_CAPABILITY, *PTWAIN_CAPABILITY;
````


## -struct-fields
<dl>

### -field lSize

<dd>
<p>Specifies the size, in bytes, of the TWAIN_CAPABILITY structure.</p>
</dd>

### -field lMSG

<dd>
<p>Specifies the particular TWAIN message, which can be one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>MSG_GET</p>
</td>
<td>
<p>Get a capability.</p>
</td>
</tr>
<tr>
<td>
<p>MSG_GETCURRENT</p>
</td>
<td>
<p>Get the current capability.</p>
</td>
</tr>
<tr>
<td>
<p>MSG_GETDEFAULT</p>
</td>
<td>
<p>Get the default capability.</p>
</td>
</tr>
<tr>
<td>
<p>MSG_RESET</p>
</td>
<td>
<p>Reset the capability.</p>
</td>
</tr>
<tr>
<td>
<p>MSG_SET</p>
</td>
<td>
<p>Set a capability.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field lCapID

<dd>
<p>Specifies the ID of the capability to set or get.</p>
</dd>

### -field lConType

<dd>
<p>Specifies the capability's container type.</p>
</dd>

### -field lRC

<dd>
<p>Specifies the TWAIN return code. This value can be on of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TWRC_FAILURE</p>
</td>
<td>
<p>The capability specified by the <b>lCapID</b> member is not supported.</p>
</td>
</tr>
<tr>
<td>
<p>TWRC_SUCCESS</p>
</td>
<td>
<p>The capability specified by the <b>lCapID</b> member is supported.</p>
</td>
</tr>
<tr>
<td>
<p>Other TWRC_XXX return code</p>
</td>
<td>
<p>See the <b>Remarks</b> section.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field lCC

<dd>
<p>Specifies the TWAIN condition code. This value can be one of the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>TWCC_BUMMER</p>
</td>
<td>
<p>The operation failed for an unknown reason.</p>
</td>
</tr>
<tr>
<td>
<p>TWCC_SUCCESS</p>
</td>
<td>
<p>The operation was successful.</p>
</td>
</tr>
<tr>
<td>
<p>TWCC_XXX</p>
</td>
<td>
<p>See the <b>Remarks</b> section.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field lDataSize

<dd>
<p>Specifies the size, in bytes of the data in the <b>Data</b> array.</p>
</dd>

### -field Data

<dd>
<p>Is an array that contains the capability data. The actual size, in bytes, of the array is indicated by the <b>lDataSize</b> member.</p>
</dd>
</dl>

## -remarks
<p>A TWAIN-capable application communicates with a WIA driver by way of the TWAIN compatibility later to find out whether the driver has any private capabilities, and if so, what they are. A TWAIN_CAPABILITY structure is used in this communication. For more information, see <a href="https://msdn.microsoft.com/270e62dd-590c-4495-be22-002957932031">TWAIN Compatibility</a>. </p>

<p>The TWAIN return codes and control codes are defined in <i>twain.h</i>, which can be obtained from the TWAIN Working Group (http://www.twain.org).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiatwcmp.h (include Wiatwcmp.h)</dt>
</dl>
</td>
</tr>
</table>