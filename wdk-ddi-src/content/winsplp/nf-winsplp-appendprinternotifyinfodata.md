---
UID: NF.winsplp.AppendPrinterNotifyInfoData
title: AppendPrinterNotifyInfoData
author: windows-driver-content
description: The print spooler's AppendPrinterNotifyInfoData function adds the contents of a specified PRINTER_NOTIFY_INFO_DATA structure to a specified PRINTER_NOTIFY_INFO structure.
old-location: print\appendprinternotifyinfodata.htm
old-project: print
ms.assetid: 558b81c5-5f6b-41a5-8d89-6ee39b9c1cd1
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: AppendPrinterNotifyInfoData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AppendPrinterNotifyInfoData
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# AppendPrinterNotifyInfoData function



## -description
<p>The print spooler's <b>AppendPrinterNotifyInfoData</b> function adds the contents of a specified PRINTER_NOTIFY_INFO_DATA structure to a specified PRINTER_NOTIFY_INFO structure.</p>


## -syntax

````
BOOL AppendPrinterNotifyInfoData(
  _In_     PPRINTER_NOTIFY_INFO      pInfoDest,
  _In_opt_ PPRINTER_NOTIFY_INFO_DATA pInfoDataSrc,
           DWORD                     fdwFlags
);
````


## -parameters
<dl>

### -param <i>pInfoDest</i> [in]

<dd>
<p>Caller-supplied pointer to a PRINTER_NOTIFY_INFO structure (defined in the Microsoft Windows SDK documentation).</p>
</dd>

### -param <i>pInfoDataSrc</i> [in, optional]

<dd>
<p>Caller-supplied pointer to a PRINTER_NOTIFY_INFO_DATA structure (defined in the Windows SDK documentation).</p>
</dd>

### -param <i>fdwFlags</i> 

<dd>
<p>Caller-supplied flags. The following flag is defined.</p>
<p></p>
<dl>

### -param <a id="PRINTER_NOTIFY_INFO_DATA_COMPACT"></a><a id="printer_notify_info_data_compact"></a>PRINTER_NOTIFY_INFO_DATA_COMPACT

<dd>
<p>If set, the function examines the <b>Type</b>, <b>Field</b>, and <b>Id</b> members of the supplied PRINTER_NOTIFY_INFO_DATA structure. If they all match an existing element of the PRINTER_NOTIFY_INFO_DATA structure array, the existing element is overwritten with the supplied element. If a match is not found, the function adds the specified structure to the end of the array.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns <b>TRUE</b>. Otherwise, the function returns <b>FALSE</b>. The caller can obtain an error code by calling GetLastError (described in the Windows SDK documentation).</p>

## -remarks
<p>A print provider's <a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a> function should call <b>AppendPrinterNotifyInfoData</b> as often as necessary to populate a PRINTER_NOTIFY_INFO_DATA structure array, after first calling <a href="..\winsplp\nf-winsplp-routerallocprinternotifyinfo.md">RouterAllocPrinterNotifyInfo</a> to allocate storage for the array and its associated PRINTER_NOTIFY_INFO structure.</p>

<p>Based on whether the PRINTER_NOTIFY_INFO_DATA_COMPACT flag is set, the function either appends the specified PRINTER_NOTIFY_INFO_DATA structure to the end of the structure array or overwrites an existing array element. If the structure is appended, the function increments the PRINTER_NOTIFY_INFO structure's <b>Count</b> member.</p>

<p>If <b>AppendPrinterNotifyInfoData</b> detects that the PRINTER_NOTIFY_INFO_DISCARDED flag is set in the specified PRINTER_NOTIFY_INFO structure, the function clears all PRINTER_NOTIFY_INFO_DATA structures and sets the error code to ERROR_OUT_OF_STRUCTURES.</p>

<p>If <b>NULL</b> is specified for <i>pInfoDataSrc</i>, <b>AppendPrinterNotifyInfoData</b> sets the PRINTER_NOTIFY_INFO_DISCARDED flag in the specified PRINTER_NOTIFY_INFO structure, clears all PRINTER_NOTIFY_INFO_DATA structures, and sets the error code to ERROR_OUT_OF_STRUCTURES.</p>

<p>(For more information about the PRINTER_NOTIFY_INFO_DISCARDED flag, see the description of FindNextPrinterChangeNotification in the Windows SDK documentation.)</p>

<p>For additional information, see <a href="NULL">Supporting Printer Change Notifications</a>.</p>

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
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.refreshprinterchangenotification">RefreshPrinterChangeNotification</a>
</dt>
<dt>
<a href="..\winsplp\nf-winsplp-routerallocprinternotifyinfo.md">RouterAllocPrinterNotifyInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20AppendPrinterNotifyInfoData function%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
