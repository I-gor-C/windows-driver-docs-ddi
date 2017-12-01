---
UID: NF.prnasntp.RouterCreatePrintAsyncNotificationChannel
title: RouterCreatePrintAsyncNotificationChannel
author: windows-driver-content
description: The RouterCreatePrintAsyncNotificationChannel function creates an asynchronous notification channel that is associated with a printer or print server.
old-location: print\routercreateprintasyncnotificationchannel.htm
old-project: print
ms.assetid: 11f9a438-861f-42ef-b4f5-f64b0b9d658a
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: RouterCreatePrintAsyncNotificationChannel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prnasntp.h
req.include-header: Prnasntp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RouterCreatePrintAsyncNotificationChannel
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

# RouterCreatePrintAsyncNotificationChannel function



## -description
<p>The <code>RouterCreatePrintAsyncNotificationChannel</code> function creates an asynchronous notification channel that is associated with a printer or print server.</p>


## -syntax

````
HRESULT RouterCreatePrintAsyncNotificationChannel(
  _In_  PCWSTR                            pName,
  _In_  PrintAsyncNotificationType        *pNotificationType,
  _In_  PrintAsyncNotifyUserFilter        eNotificationFilter,
  _In_  PrintAsyncNotifyConversationStyle eConversationStyle,
  _In_  IPrintAsyncNotifyCallback         *pCallback,
  _Out_ IPrintAsyncNotifyChannel          **ppIAsyncNotification
);
````


## -parameters
<dl>

### -param <i>pName</i> [in]

<dd>
<p>A pointer to a null-terminated string that specifies the name of the printer or print server.</p>
</dd>

### -param <i>pNotificationType</i> [in]

<dd>
<p>A pointer to a GUID that represents the type of notifications sent through this channel.</p>
</dd>

### -param <i>eNotificationFilter</i> [in]

<dd>
<p>A filter for the session or user that receives the notifications.</p>
</dd>

### -param <i>eConversationStyle</i> [in]

<dd>
<p>The type of communication: unidirectional or bidirectional.</p>
</dd>

### -param <i>pCallback</i> [in]

<dd>
<p>A pointer to the callback function that is called to deliver the response notifications, when bidirectional communication is in effect. This parameter is ignored when unidirectional communication is in effect.</p>
</dd>

### -param <i>ppIAsyncNotification</i> [out]

<dd>
<p>A pointer to a variable that receives the address of the interface object that represents the notification channel.</p>
</dd>
</dl>

## -returns
<p><code>RouterCreatePrintAsyncNotificationChannel</code> returns S_OK on success and returns a standard COM error code otherwise.</p>

## -remarks
<p>In some cases, you must release the channel that you created with the <code>RouterCreatePrintAsyncNotificationChannel</code> function by calling <b>Release</b> on IPrintAsyncNotifyChannel. For information about when to release a channel, see <a href="NULL">Notification Channel</a>.</p>

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
<dt>Prnasntp.h (include Prnasntp.h)</dt>
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