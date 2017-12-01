---
UID: NN.bidispl.IBidiRequestContainer~r1
title: IBidiRequestContainer
author: windows-driver-content
description: The IBidiRequestContainer interface allows an application or other objects to compose and retrieve a list of bidi requests.
old-location: print\ibidirequestcontainer.htm
old-project: print
ms.assetid: 21dfcbe8-2fc1-4495-af54-5d4c83b8bb79
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiRequestContainer
req.alt-loc: Bidispl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IBidiSpl2
---

# IBidiRequestContainer interface



## -description
<p>The <b>IBidiRequestContainer</b> interface allows an application or other objects to compose and retrieve a list of bidi requests.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IBidiRequestContainer</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IBidiRequestContainer</b> also has these types of members:</p>

<p>The <b>IBidiRequestContainer</b> interface has these methods.</p>

<p>Adds a request to the request list.</p>

<p>Enumerates the number of requests in the list.</p>

<p>Gets the number of requests in the list.</p>

<p> </p>

## -members
<p>The <b>IBidiRequestContainer</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidirequestcontainer_ibidirequestcontainer__addrequest">AddRequest</a>
</td>
<td align="left" width="63%">
<p>Adds a request to the request list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidirequestcontainer_ibidirequestcontainer__getenumobject">GetEnumObject</a>
</td>
<td align="left" width="63%">
<p>Enumerates the number of requests in the list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidirequestcontainer_ibidirequestcontainer__getrequestcount">GetRequestCount</a>
</td>
<td align="left" width="63%">
<p>Gets the number of requests in the list.</p>
</td>
</tr>
</table><p>Adds a request to the request list.</p>

<p>Enumerates the number of requests in the list.</p>

<p>Gets the number of requests in the list.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows XP</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2003</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="print.bidirectional_communication_interfaces">Bidirectional Communication Interfaces</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/42b5e6cf-b434-4734-86f3-b3b9d15ea468">Print Spooler Components</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiRequestContainer interface%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
