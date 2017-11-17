---
UID: NN.bidispl.IBidiSpl2~r1
title: IBidiSpl2
author: windows-driver-content
description: The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.
old-location: print\ibidispl2.htm
ms.assetid: 90e8a390-7d30-4bcf-8c81-438c86529ceb
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: print
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiSpl2
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
ms.keywords: IBidiSpl2, UnbindDevice, IBidiSpl2::UnbindDevice
req.iface: IBidiSpl2
---

# IBidiSpl2 interface



## -description
<p>The <b>IBidiSpl2</b> interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IBidiSpl2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IBidiSpl2</b> also has these types of members:</p>

<p>The <b>IBidiSpl2</b> interface has these methods.</p>

<p>Binds a printer to a bidirectional communication request.</p>

<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.</p>

<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.</p>

<p>Releases a printer from a bidirectional communication request.</p>

<p> </p>

## -members
<p>The <b>IBidiSpl2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/c5bd238d-4b85-4463-aa73-ff3a7798ccff">BindDevice</a>
</td>
<td align="left" width="63%">
<p>Binds a printer to a bidirectional communication request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/2daf99a8-42dc-4739-8e7e-80d3c9a084b7">SendRecvXMLStream</a>
</td>
<td align="left" width="63%">
<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/7d61402e-e248-4770-a828-9c266e528115">SendRecvXMLString</a>
</td>
<td align="left" width="63%">
<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/26f3fc82-051d-4827-8b59-ac2c99f4d2c5">UnbindDevice</a>
</td>
<td align="left" width="63%">
<p>Releases a printer from a bidirectional communication request.</p>
</td>
</tr>
</table><p>Binds a printer to a bidirectional communication request.</p>

<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.</p>

<p>Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.</p>

<p>Releases a printer from a bidirectional communication request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>
</dt>
<dt>
<a href="NULL">Bidirectional Communication Schema</a>
</dt>
<dt>
<a href="NULL">Print Spooler Components</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2 interface%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
