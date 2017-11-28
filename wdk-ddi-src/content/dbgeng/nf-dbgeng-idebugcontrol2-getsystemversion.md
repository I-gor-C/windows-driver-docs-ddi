---
UID: NF.dbgeng.IDebugControl2.GetSystemVersion
title: IDebugControl2::GetSystemVersion
author: windows-driver-content
description: The GetSystemVersion method returns information that identifies the operating system on the computer that is running the current target.
old-location: debugger\getsystemversion.htm
old-project: debugger
ms.assetid: 9418ac12-3de0-4477-a725-437700c4d83c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, GetSystemVersion, IDebugControl2::GetSystemVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h, Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetSystemVersion,IDebugControl2.GetSystemVersion,IDebugControl3.GetSystemVersion
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
req.iface: IDebugControl2
---

# IDebugControl2::GetSystemVersion method



## -description
<p>The <b>GetSystemVersion</b> method returns information that identifies the operating system on the computer that is running the current target.</p>


## -syntax

````
HRESULT GetSystemVersion(
  [out]           PULONG PlatformId,
  [out]           PULONG Major,
  [out]           PULONG Minor,
  [out, optional] PSTR   ServicePackString,
  [in]            ULONG  ServicePackStringSize,
  [out, optional] PULONG ServicePackStringUsed,
  [out]           PULONG ServicePackNumber,
  [out, optional] PSTR   BuildString,
  [in]            ULONG  BuildStringSize,
  [out, optional] PULONG BuildStringUsed
);
````


## -parameters
<dl>

### -param <i>PlatformId</i> [out]

<dd>
<p>Receives the platform ID. <i>PlatformId</i> is always VER_PLATFORM_WIN32_NT for NT-based Windows.   </p>
</dd>

### -param <i>Major</i> [out]

<dd>
<p>Receives 0xF if the target's operating system is a <a href="wdkgloss.f#wdkgloss.free_build#wdkgloss.free_build"><i>free build</i></a>, or 0xC if the operating system is a <a href="wdkgloss.c#wdkgloss.checked_build#wdkgloss.checked_build"><i>checked build</i></a>.</p>
</dd>

### -param <i>Minor</i> [out]

<dd>
<p>Receives the build number for the target's operating system.</p>
</dd>

### -param <i>ServicePackString</i> [out, optional]

<dd>
<p>Receives the string for the service pack level of the target computer.  If <i>ServicePackString</i> is <b>NULL</b>, this information is not returned.  If no service pack is installed, <i>ServicePackString</i> can be empty.</p>
</dd>

### -param <i>ServicePackStringSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>ServicePackString</i> specifies.</p>
</dd>

### -param <i>ServicePackStringUsed</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the string of the service pack level.  If <i>ServicePackStringUsed</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>ServicePackNumber</i> [out]

<dd>
<p>Receives the service pack level of the target's operating system.</p>
</dd>

### -param <i>BuildString</i> [out, optional]

<dd>
<p>Receives the string that identifies the build of the system.  If <i>BuildString</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BuildStringSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the buffer that <i>BuildString</i> specifies.</p>
</dd>

### -param <i>BuildStringUsed</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the string that identifies the build.  If <i>BuildStringUsed</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the <i>ServicePackString</i> buffer or the <i>BuildString</i> buffer were too small and the corresponding string was truncated.</p>

<p> </p>

## -remarks
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558860">Target Information</a>.</p>

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
<dt>Dbgeng.h (include Dbgeng.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549245">GetSystemVersionString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549258">GetSystemVersionValues</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetSystemVersion method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
