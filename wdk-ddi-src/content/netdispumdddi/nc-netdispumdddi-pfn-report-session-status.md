---
UID: NC.netdispumdddi.PFN_REPORT_SESSION_STATUS
title: PFN_REPORT_SESSION_STATUS
author: windows-driver-content
description: Called by the user-mode display driver to report the status of the current Miracast connected session.The data type of this function is PFN_REPORT_SESSION_STATUS.
old-location: display\reportsessionstatus.htm
old-project: display
ms.assetid: a3e44e55-5c6a-4a79-8caa-3a3b9db6b456
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ReportSessionStatus
req.alt-loc: Netdispumdddi.h
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
---

# PFN_REPORT_SESSION_STATUS callback



## -description
<p>Called by the user-mode display driver to report the status of the current Miracast connected session.<p>The data type of this function is <b>PFN_REPORT_SESSION_STATUS</b>.</p>
</p>
<p>The data type of this function is <b>PFN_REPORT_SESSION_STATUS</b>.</p>


## -prototype

````
PFN_REPORT_SESSION_STATUS ReportSessionStatus;

VOID ReportSessionStatus(
  _In_ HANDLE          hMiracastDeviceHandle,
  _In_ MIRACAST_STATUS MiracastStatus,
  _In_ NTSTATUS        Status
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMiracastDeviceHandle</i> [in]

<dd>
<p>A handle that represents a Miracast device. The Miracast user-mode driver previously obtained this handle as the <i>hMiracastDeviceHandle</i> parameter in a call to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> function.</p>
</dd>

### -param <i>MiracastStatus</i> [in]

<dd>
<p>The current status of the Miracast link, of type <a href="..\netdispumdddi\ne-netdispumdddi-miracast-status.md">MIRACAST_STATUS</a>.</p>
</dd>

### -param <i>Status</i> [in]

<dd>
<p>A status value the driver can provide that's logged for diagnostics purposes.</p>
</dd>
</dl>

## -returns
<p>Does not return a value.</p>

## -remarks
<p>If the Miracast user-mode driver reports an error in the <i>MiracastStatus</i> parameter, it initiates a tear-down of the current Miracast connected session.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a>
</dt>
<dt>
<a href="..\netdispumdddi\ne-netdispumdddi-miracast-status.md">MIRACAST_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_REPORT_SESSION_STATUS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
