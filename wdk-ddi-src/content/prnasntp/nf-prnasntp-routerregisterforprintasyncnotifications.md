---
UID: NF.prnasntp.RouterRegisterForPrintAsyncNotifications
title: RouterRegisterForPrintAsyncNotifications
author: windows-driver-content
description: The RouterRegisterForPrintAsyncNotifications function registers for asynchronous notifications associated with a printer or print server.
old-location: print\routerregisterforprintasyncnotifications.htm
ms.assetid: 87966827-72b2-4be7-859a-628c1accca48
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prnasntp.h
req.include-header: Prnasntp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RouterRegisterForPrintAsyncNotifications
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
ms.keywords: RouterRegisterForPrintAsyncNotifications
req.iface: 
req.product: Windows 10 or later.
---

# RouterRegisterForPrintAsyncNotifications function



## -description
<p>The <code>RouterRegisterForPrintAsyncNotifications</code> function registers for asynchronous notifications associated with a printer or print server.</p>


## -syntax

````
HRESULT RouterRegisterForPrintAsyncNotifications(
  _In_  PCWSTR                            pName,
  _In_  PrintAsyncNotificationType        *pNotificationType,
  _In_  PrintAsyncNotifyUserFilter        eNotifyFilter,
  _In_  PrintAsyncNotifyConversationStyle eConversationStyle,
  _In_  IPrintAsyncNotifyCallback         *pCallback,
  _Out_ HANDLE                            *phNotify
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
<p>A pointer to the GUID that represents the type of notifications of interest to the caller.</p>
</dd>

### -param <i>eNotifyFilter</i> [in]

<dd>
<p>The filter for the session or user of interest to the caller when receiving notifications.</p>
</dd>

### -param <i>eConversationStyle</i> [in]

<dd>
<p>The type of communication: unidirectional or bidirectional.</p>
</dd>

### -param <i>pCallback</i> [in]

<dd>
<p>A pointer to the callback that is used deliver the notifications.</p>
</dd>

### -param <i>phNotify</i> [out]

<dd>
<p>A pointer to an opaque handle. The caller can use this handle to discontinue receiving notifications.</p>
</dd>
</dl>

## -returns
<p>This function returns S_OK on success, and a standard COM error code otherwise.</p>

## -remarks


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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562028">RouterUnregisterForPrintAsyncNotifications</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20RouterRegisterForPrintAsyncNotifications function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
