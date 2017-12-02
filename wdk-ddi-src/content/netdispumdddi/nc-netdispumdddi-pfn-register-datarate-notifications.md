---
UID: NC.netdispumdddi.PFN_REGISTER_DATARATE_NOTIFICATIONS
title: PFN_REGISTER_DATARATE_NOTIFICATIONS
author: windows-driver-content
description: Called by the user-mode driver to register with the operating system to receive network quality of service (QoS) notifications and the current network bandwidth of the Miracast connection.The data type of this function is PFN_REGISTER_DATARATE_NOTIFICATIONS.
old-location: display\registerfordataratenotifications.htm
old-project: display
ms.assetid: 81500bb9-27f1-4688-b244-37dfd766f3c8
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
req.alt-api: RegisterForDataRateNotifications
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

# PFN_REGISTER_DATARATE_NOTIFICATIONS callback



## -description
<p>Called by the user-mode driver to register with the operating system to receive network quality of service (QoS) notifications and the current  network bandwidth of the Miracast connection.<p>The data type of this function is <b>PFN_REGISTER_DATARATE_NOTIFICATIONS</b>.</p>
</p>
<p>The data type of this function is <b>PFN_REGISTER_DATARATE_NOTIFICATIONS</b>.</p>


## -prototype

````
PFN_REGISTER_DATARATE_NOTIFICATIONS RegisterForDataRateNotifications;

NTSTATUS RegisterForDataRateNotifications(
  _In_     HANDLE                    hMiracastDeviceHandle,
  _In_opt_ PVOID                     pNotificationContext,
  _In_opt_ PFN_DATARATE_NOTIFICATION pfnDataRateNotify
)
{ ... }
````


## -parameters
<dl>

### -param hMiracastDeviceHandle [in]

<dd>
<p>A handle that represents a Miracast device. The Miracast user-mode driver previously obtained this handle as the <i>hMiracastDeviceHandle</i> parameter in a call to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-create-miracast-context.md">CreateMiracastContext</a> function.</p>
</dd>

### -param pNotificationContext [in, optional]

<dd>
<p>The context that will be passed to the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-datarate-notification.md">pfnDataRateNotify</a> function when the Miracast data rate changes.</p>
</dd>

### -param pfnDataRateNotify [in, optional]

<dd>
<p>A pointer to the driver routine that will be called when the bit rate of the Miracast network link has changed. See Remarks for more info.</p>
<p>  The driver can supply a <b>NULL</b> value to unregister for notifications.</p>
</dd>
</dl>

## -returns
<p>If the operating system successfully registers or unregisters the driver for notifications, it returns <b>STATUS_SUCCESS</b>.</p>

<p>Otherwise, these error codes can be returned:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One or more parameters are invalid.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The operating system cannot support quality of service (QoS) notifications, or the call to the function is made outside of the calling thread in which the operating system called <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a> or <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> functions.</p>

<p> </p>

## -remarks
<p>The user-mode driver can optionally call this function to register for automatic calls to data rate notification callback functions once a second.</p>

<p>To unregister from notifications, the driver should supply a value of <b>NULL</b> for the <i>pfnDataRateNotify</i> parameter and for the <b>CurrentBitRate</b> member of the <a href="..\netdispumdddi\ns-netdispumdddi-miracast-wfd-connection-stats.md">MIRACAST_WFD_CONNECTION_STATS</a> structure
pointed to by the <i>pWfdConnectionStats</i> parameter when it calls the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a> function. When the operating system receives <b>NULL</b> for both <i>pfnDataRateNotify</i> and <b>CurrentBitRate</b>, it will no longer provide notifications.</p>

<p>Also, if the operating system can no longer provide QoS data, it sets the <i>pDataRateStats</i> parameter to <b>NULL</b> when the <a href="..\netdispumdddi\nc-netdispumdddi-pfn-datarate-notification.md">pfnDataRateNotify</a>  function is called.</p>

<p>The function fails if the driver attempts to register while it is already registered, or if it attempts to unregister if it has already unregistered. The function fails if the call is made outside of the calling thread in which the operating system called <a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a> or <a href="..\netdispumdddi\nc-netdispumdddi-pfn-stop-miracast-session.md">StopMiracastSession</a> functions.</p>

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
<a href="..\netdispumdddi\ns-netdispumdddi-miracast-wfd-connection-stats.md">MIRACAST_WFD_CONNECTION_STATS</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-datarate-notification.md">pfnDataRateNotify</a>
</dt>
<dt>
<a href="..\netdispumdddi\nc-netdispumdddi-pfn-start-miracast-session.md">StartMiracastSession</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFN_REGISTER_DATARATE_NOTIFICATIONS callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
