---
UID: NS.wiamicro.VAL
title: VAL
author: windows-driver-content
description: The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other.
old-location: image\val.htm
ms.assetid: 9c9cf520-3249-4c1e-9d0d-e07f7127117e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: image
req.header: wiamicro.h
req.include-header: Wiamicro.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VAL
req.alt-loc: wiamicro.h
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
ms.keywords: VAL, VAL, *PVAL
req.iface: 
req.product: Windows 10 or later.
---

# VAL structure



## -description
<p>The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other.</p>


## -syntax

````
typedef struct VAL {
  LONG      lVal;
  double    dblVal;
  GUID      *pGuid;
  PSCANINFO pScanInfo;
  HGLOBAL   handle;
  WCHAR     **ppButtonNames;
  HANDLE    *pHandle;
  LONG      lReserved;
  CHAR      szVal[MAX_ANSI_CHAR];
} VAL, *PVAL;
````


## -struct-fields
<dl>

### -field <b>lVal</b>

<dd>
<p>Specifies a command value to return to the WIA Flatbed driver. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff552714">WIA Microdriver Commands</a> for a list of available commands for this parameter.</p>
</dd>

### -field <b>dblVal</b>

<dd>
<p>Specifies a command value to return to the WIA Flatbed driver. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff552714">WIA Microdriver Commands</a> for a list of available commands for this parameter.</p>
</dd>

### -field <b>pGuid</b>

<dd>
<p>Points to the GUID of the pressed button. If no button was pressed, this member points to GUID_NULL.</p>
</dd>

### -field <b>pScanInfo</b>

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547361">SCANINFO</a> structure.</p>
</dd>

### -field <b>handle</b>

<dd>
<p>Points to a ShutDown event handle that will be signaled by the WIA Flatbed Driver when the driver is being unloaded or shut down. </p>
</dd>

### -field <b>ppButtonNames</b>

<dd>
<p>Specifies the address of a pointer to an array of button names.</p>
</dd>

### -field <b>pHandle</b>

<dd>
<p>Points to an event handle.</p>
</dd>

### -field <b>lReserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>szVal</b>

<dd>
<p>Specifies the device name in ASCII form. If needed for interrupt checking, the microdriver can use this name to pass to <a href="fs.createfile">CreateFile</a> (described in the Microsoft Windows SDK documentation) in order to obtain a file handle to the device.</p>
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
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamicro.h (include Wiamicro.h)</dt>
</dl>
</td>
</tr>
</table>