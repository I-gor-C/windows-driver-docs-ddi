---
UID: NS.d3dumddi._D3DDDIARG_QUERYAUTHENICATEDCHANNEL
title: D3DDDIARG_QUERYAUTHENICATEDCHANNEL
author: windows-driver-content
description: The D3DDDIARG_QUERYAUTHENTICATEDCHANNEL structure describes authenticated-channel information to query by using the QueryAuthenticatedChannel function.
old-location: display\d3dddiarg_queryauthenticatedchannel.htm
ms.assetid: d816b4d7-cc99-4a83-9fd2-c7c0659d0318
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_QUERYAUTHENTICATEDCHANNEL is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_QUERYAUTHENTICATEDCHANNEL
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDIARG_QUERYAUTHENICATEDCHANNEL, D3DDDIARG_QUERYAUTHENTICATEDCHANNEL
req.iface: 
---

# D3DDDIARG_QUERYAUTHENICATEDCHANNEL structure



## -description
<p>The D3DDDIARG_QUERYAUTHENTICATEDCHANNEL structure describes authenticated-channel information to query by using the <a href="https://msdn.microsoft.com/13b65b5a-9512-4d67-b629-479bdd74674e">QueryAuthenticatedChannel</a> function. </p>


## -syntax

````
typedef struct _D3DDDIARG_QUERYAUTHENTICATEDCHANNEL {
  UINT       InputSize;
  const VOID *pInputData;
  UINT       OutputSize;
  VOID       *pOutputData;
} D3DDDIARG_QUERYAUTHENTICATEDCHANNEL;
````


## -struct-fields
<dl>

### -field <b>InputSize</b>

<dd>
<p>[in] The size, in bytes, of the input data that the <b>pInputData</b> member points to. </p>
</dd>

### -field <b>pInputData</b>

<dd>
<p>[in] A pointer to a buffer that describes the information to query. The buffer that <b>pInputData</b> points to is defined identically to the input buffer that is passed to the <b>IDirect3DAuthenticatedChannel::Query</b> method. For more information about <b>IDirect3DAuthenticatedChannel::Query</b>, see the Windows SDK documentation. </p>
</dd>

### -field <b>OutputSize</b>

<dd>
<p>[in] The size, in bytes, of the output data that the <b>pOutputData</b> member points to. </p>
</dd>

### -field <b>pOutputData</b>

<dd>
<p>[in/out] A pointer to a buffer that describes the information that the <a href="https://msdn.microsoft.com/13b65b5a-9512-4d67-b629-479bdd74674e">QueryAuthenticatedChannel</a> function returns. The buffer that <b>pOutputData</b> points to is defined identically to the output buffer that the <b>IDirect3DAuthenticatedChannel::Query</b> method returns. </p>
</dd>
</dl>

## -remarks
<p>The definitions of the input and output buffers to which the <b>pInputData</b> and <b>pOutputData</b> members point, depend on the type of information. The first member of the input buffer is always a D3DAUTHENTICATEDCHANNEL_QUERY_INPUT structure, whose <b>QueryType</b> member identifies the type of information to query.</p>

<p>The definition of the output buffer also depends on the information that the <a href="https://msdn.microsoft.com/13b65b5a-9512-4d67-b629-479bdd74674e">QueryAuthenticatedChannel</a> function queries. However, the first member of the output buffer is always a D3DAUTHENTICATEDCHANNEL_QUERY_OUTPUT structure, whose members specify the following information:</p>

<p>The <b>omac</b> member identifies the One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) that permits the caller to authenticate the entire buffer, which prevents man-in-the-middle attacks.</p>

<p>The <b>QueryType</b>, <b>hChannel</b>, and <b>SequenceNumber</b> members from the input buffer prevent against replay attacks. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_QUERYAUTHENTICATEDCHANNEL is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/13b65b5a-9512-4d67-b629-479bdd74674e">QueryAuthenticatedChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_QUERYAUTHENTICATEDCHANNEL structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
