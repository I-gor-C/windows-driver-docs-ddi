---
UID: NN.bidispl.IBidiRequest~r1
title: IBidiRequest
author: windows-driver-content
description: The IBidiRequest interface allows an application or other objects to compose a bidi request.
old-location: print\ibidirequest.htm
ms.assetid: e7b16853-7f1d-45e4-af5e-4ae9cbb9b191
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: print
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiRequest
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

# IBidiRequest interface



## -description
<p>The <b>IBidiRequest</b> interface allows an application or other objects to compose a bidi request.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IBidiRequest</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IBidiRequest</b> also has these types of members:</p>

<p>The <b>IBidiRequest</b> interface has these methods.</p>

<p>Gets the number of output items.</p>

<p>Gets the output data coming back from the device.</p>

<p>Gets the result code.</p>

<p>Sets the data to send to the device.</p>

<p>Sets the bidi schema string.</p>

<p> </p>

## -members
<p>The <b>IBidiRequest</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/4c857ff4-02c1-487b-bdb0-44d62a4cf4a1">GetEnumCount</a>
</td>
<td align="left" width="63%">
<p>Gets the number of output items.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/0757dbc2-850b-4267-9339-b87591f85767">GetOutputData</a>
</td>
<td align="left" width="63%">
<p>Gets the output data coming back from the device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/d3d37fd2-b3fa-4664-ba4b-c355197d9b40">GetResult</a>
</td>
<td align="left" width="63%">
<p>Gets the result code.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/8db7b5cd-b03f-4973-8711-8ac022bfb2b5">SetInputData</a>
</td>
<td align="left" width="63%">
<p>Sets the data to send to the device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/ca4f7ea4-fcad-42b0-a63a-eee3706e5cbf">SetSchema</a>
</td>
<td align="left" width="63%">
<p>Sets the bidi schema string.</p>
</td>
</tr>
</table><p>Gets the number of output items.</p>

<p>Gets the output data coming back from the device.</p>

<p>Gets the result code.</p>

<p>Sets the data to send to the device.</p>

<p>Sets the bidi schema string.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiRequest interface%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
