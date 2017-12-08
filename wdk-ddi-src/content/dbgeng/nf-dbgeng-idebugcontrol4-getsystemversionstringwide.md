---
UID: NF.dbgeng.IDebugControl4.GetSystemVersionStringWide
title: IDebugControl4::GetSystemVersionStringWide
author: windows-driver-content
description: The GetSystemVersionStringWide method returns a string that describes the target's operating system version.
old-location: debugger\getsystemversionstringwide.htm
old-project: debugger
ms.assetid: a98dee8a-1911-40e0-b1fd-c7a1ee40a8d7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl4, GetSystemVersionStringWide, IDebugControl4::GetSystemVersionStringWide
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl4.GetSystemVersionStringWide
req.alt-loc: dbgeng.h
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
req.iface: IDebugControl4
---

# IDebugControl4::GetSystemVersionStringWide method



## -description
<p>The <b>GetSystemVersionStringWide</b>  method returns a string that describes the target's operating system version.</p>


## -syntax

````
HRESULT GetSystemVersionStringWide(
  [in]            ULONG  Which,
  [out, optional] PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG StringSize
);
````


## -parameters
<dl>

### -param Which [in]

<dd>
<p>Specifies which version string to return.  The possible values are listed in the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Version string</th>
</tr>
<tr>
<td>
<p>DEBUG_SYSVERSTR_SERVICE_PACK</p>
</td>
<td>
<p>Returns a description of the service pack for the target's operating system.  For example, "Service Pack 1".</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYSVERSTR_BUILD</p>
</td>
<td>
<p>Returns a description of the target's operating system build version.  For example, "kernel32.dll version: 5.1.2600.1106 (xpsp1.020828-1920)".</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param Buffer [out, optional]

<dd>
<p>Receives the version string.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>Buffer</i> specifies.</p>
</dd>

### -param StringSize [out, optional]

<dd>
<p>Receives the size, in characters, of the string that identifies the build.  If <i>SizeString</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the buffer was too small, so the string was truncated.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugcontrol4.md">IDebugControl4</a>
</dt>
<dt>
<a href="debugger.getsystemversion">GetSystemVersion</a>
</dt>
<dt>
<a href="debugger.getsystemversionvalues">GetSystemVersionValues</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl4::GetSystemVersionStringWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
