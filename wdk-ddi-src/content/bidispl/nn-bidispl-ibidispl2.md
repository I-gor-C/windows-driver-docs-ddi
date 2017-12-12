---
UID: NN.bidispl.IBidiSpl2
title: IBidiSpl2
author: windows-driver-content
description: The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.
old-location: print\ibidispl2.htm
old-project: print
ms.assetid: 90e8a390-7d30-4bcf-8c81-438c86529ceb
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: _MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE, MPEG2_TRANSPORT_STRIDE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
---

# IBidiSpl2 interface



## -description
The <b>IBidiSpl2</b> interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IBidiSpl2</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IBidiSpl2</b> also has these types of members:

The <b>IBidiSpl2</b> interface has these methods.

Binds a printer to a bidirectional communication request.

Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.

Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.

Releases a printer from a bidirectional communication request.

 


## -members
The <b>IBidiSpl2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidispl2_ibidispl2__binddevice">BindDevice</a>
</td>
<td align="left" width="63%">
Binds a printer to a bidirectional communication request.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidispl2_ibidispl2__sendrecvxmlstream">SendRecvXMLStream</a>
</td>
<td align="left" width="63%">
Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidispl2_ibidispl2__sendrecvxmlstring">SendRecvXMLString</a>
</td>
<td align="left" width="63%">
Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="print.ibidispl2_ibidispl2__unbinddevice">UnbindDevice</a>
</td>
<td align="left" width="63%">
Releases a printer from a bidirectional communication request.

</td>
</tr>
</table>Binds a printer to a bidirectional communication request.

Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant <a href="stg.istream">IStream</a>.

Sends a bidirectional communication request (and receives the response) as   Bidi Request and Response-compliant strings.

Releases a printer from a bidirectional communication request.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows Vista

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2008

</td>
</tr>
<tr>
<th width="30%">
Header

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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2 interface%20 RELEASE:%20(12/9/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

