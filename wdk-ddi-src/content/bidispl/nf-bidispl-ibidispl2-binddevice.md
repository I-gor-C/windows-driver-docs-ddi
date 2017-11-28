---
UID: NF.bidispl.IBidiSpl2.BindDevice
title: IBidiSpl2::BindDevice
author: windows-driver-content
description: The IBidiSpl2::BindDevice method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the OpenPrinter function.
old-location: print\ibidispl2_ibidispl2__binddevice.htm
old-project: print
ms.assetid: c5bd238d-4b85-4463-aa73-ff3a7798ccff
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IBidiSpl2, BindDevice, IBidiSpl2::BindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: bidispl.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiSpl2.IBidiSpl2::BindDevice
req.alt-loc: bidispl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Bidispl.dll
req.irql: PASSIVE_LEVEL
req.iface: IBidiSpl2
---

# IBidiSpl2::BindDevice method



## -description
<p>The <b>IBidiSpl2::BindDevice</b> method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the <a href="NULL">OpenPrinter</a> function.</p>


## -syntax

````
HRESULT IBidiSpl2::BindDevice(
  [in] const LPCWSTR pszDeviceName,
  [in] const DWORD   dwAccess
);
````


## -parameters
<dl>

### -param <i>pszDeviceName</i> [in]

<dd>
<p>A pointer to a null-terminated string that contains the name of the printer or print server. If <b>NULL</b>, this parameter indicates the local print server.</p>
</dd>

### -param <i>dwAccess</i> [in]

<dd>
<p>The access privileges for the printer. This parameter can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="BIDI_ACCESS_ADMINISTRATOR"></a><a id="bidi_access_administrator"></a><dl>

### -param <b>BIDI_ACCESS_ADMINISTRATOR</b>

</dl>
</td>
<td width="60%">
<p>Permits users to perform all administrative tasks and basic printing operations except for SYNCHRONIZE. This is the same as PRINTER_ALL_ACCESS in <a href="NULL">OpenPrinter</a>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_ACCESS_USER"></a><a id="bidi_access_user"></a><dl>

### -param <b>BIDI_ACCESS_USER</b>

</dl>
</td>
<td width="60%">
<p>Permits users to perform basic printing operations. This is the same as PRINTER_ACCESS_USE in <a href="NULL">OpenPrinter</a>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>The method returns one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successful.</p><dl>
<dt><b>E_HANDLE</b></dt>
</dl><p>The interface handle is invalid.</p><dl>
<dt><b>None of the above</b></dt>
</dl><p>The <b>HRESULT</b> contains an error code that corresponds to the last error.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2008</p>
</td>
</tr>
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
<dt>Bidispl.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Bidispl.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dd144981">IBidiSpl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>
</dt>
<dt>
<a href="NULL">Bidirectional Communication Schema</a>
</dt>
<dt>
<a href="NULL">Print Spooler Components</a>
</dt>
<dt>
<a href="NULL">OpenPrinter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2::IBidiSpl2::BindDevice method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
