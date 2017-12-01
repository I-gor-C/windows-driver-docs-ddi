---
UID: NF.winddiui.DrvDriverEvent
title: DrvDriverEvent
author: windows-driver-content
description: The print spooler calls a printer interface DLL's DrvDriverEvent function when the spooler processes driver-specific events that might require action by the printer driver.
old-location: print\drvdriverevent.htm
old-project: print
ms.assetid: 84d1f438-b6ee-4199-89ae-9384601203b3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DrvDriverEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrvDriverEvent
req.alt-loc: winddiui.h
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
req.iface: 
req.product: Windows 10 or later.
---

# DrvDriverEvent function



## -description
<p>The print spooler calls a printer interface DLL's <b>DrvDriverEvent</b> function when the spooler processes driver-specific events that might require action by the printer driver.</p>


## -syntax

````
BOOL DrvDriverEvent(
           DWORD  dwDriverEvent,
           DWORD  dwLevel,
  _In_opt_ LPBYTE pDriverInfo,
           LPARAM lParam
);
````


## -parameters
<dl>

### -param <i>dwDriverEvent</i> 

<dd>
<p>Caller-supplied bit flag indicating the event that has occurred. Valid flags are listed in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>DRIVER_EVENT_DELETE</p>
</td>
<td>
<p>The driver is being removed.</p>
</td>
</tr>
<tr>
<td>
<p>DRIVER_EVENT_INITIALIZE</p>
</td>
<td>
<p>The driver has just been installed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>dwLevel</i> 

<dd>
<p>Caller-supplied value indicating the type of structure pointed to by the <i>pDriverInfo</i> parameter, as indicated in the following table.</p>
<table>
<tr>
<th><i>dwLevel</i> Value</th>
<th>Structure pointed to by <i>pDriverInfo</i></th>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>DRIVER_INFO_1</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>DRIVER_INFO_2</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>DRIVER_INFO_3</p>
</td>
</tr>
</table>
<p> </p>
<dl>
<dd>
<p>The DRIVER_INFO_<i>N</i> structures are described in the Microsoft Windows SDK documentation.</p>
</dd>
</dl>
</dd>

### -param <i>pDriverInfo</i> [in, optional]

<dd>
<p>Caller-supplied pointer to a structure whose type is identified by the <i>dwLevel</i> parameter. </p>
</dd>

### -param <i>lParam</i> 

<dd>
<p>Caller-supplied flags. See the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. Otherwise, it should return <b>FALSE</b>.</p>

## -remarks
<p>The optional <b>DrvDriverEvent</b> function is called by the spooler's <b>AddPrinterDriverEx</b> and <b>DeletePrinterDriverEx</b> functions, which are described in the Windows SDK documentation.</p>

<p>The function's purpose is to allow a printer driver's <a href="NULL">printer interface DLL</a> to perform operations needed when the driver is installed or removed. A typical operation for this function to perform is to create or remove extra driver-specific files that are not specified as dependent files in a <a href="https://msdn.microsoft.com/33f1c836-0846-49d5-8ab5-baadf9e0678c">printer INF file</a>.</p>

<p>If <i>dwDriverEvent</i> is DRIVER_EVENT_DELETE, the <i>lparam</i> parameter contains the flags that were specified for the <b>DeletePrinterDriverEx</b> function's <i>dwDeleteFlag</i> parameter. The <i>lparam</i> parameter is not used if <i>dwDriverEvent</i> is DRIVER_EVENT_INITIALIZE.</p>

<p>Because the <b>DrvDriverEvent</b> function is called in the context of the print spooler, it cannot display a user interface.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winddiui.h (include Winddiui.h)</dt>
</dl>
</td>
</tr>
</table>