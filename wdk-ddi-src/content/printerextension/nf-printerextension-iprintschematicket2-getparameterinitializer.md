---
UID: NF.printerextension.IPrintSchemaTicket2.GetParameterInitializer
title: IPrintSchemaTicket2::GetParameterInitializer
author: windows-driver-content
description: The GetParameterInitializer method retrieves the IPrintSchemaParameterInitializer object, and it represents the &lt;psf:ParameterInit&gt; element in the PrintTicket XML.
old-location: print\iprintschematicket2_getparameterinitializer.htm
old-project: print
ms.assetid: E5403359-A757-4530-B17B-C80E8A45AA92
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintSchematicket2.GetParameterInitializer
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrintSchemaTicket2::GetParameterInitializer method



## -description
<p>The <b>GetParameterInitializer</b> method retrieves the <a href="..\printerextension\nn-printerextension-iprintschemaparameterinitializer.md">IPrintSchemaParameterInitializer</a> object, and it  represents the &lt;psf:ParameterInit&gt; element in the PrintTicket XML.</p>
<p>The keyword name and keyword namespace URI specify the <b>IPrintSchemaParameterInitializer</b> object to be retrieved.</p>


## -syntax

````
HRESULT GetParameterInitializer(
  [in]          BSTR                             bstrName,
  [in]          BSTR                             bstrNamespaceUri,
  [out, retval] IPrintSchemaParameterInitializer **ppParameterInitializer
);
````


## -parameters
<dl>

### -param <i>bstrName</i> [in]

<dd>
<p>The keyword name.</p>
</dd>

### -param <i>bstrNamespaceUri</i> [in]

<dd>
<p>The keyword namespace URI.</p>
</dd>

### -param <i>ppParameterInitializer</i> [out, retval]

<dd>
<p>The <a href="..\printerextension\nn-printerextension-iprintschemaparameterinitializer.md">IPrintSchemaParameterInitializer</a> object.</p>
</dd>
</dl>

## -returns
<p>The <b>GetParameterInitializer</b> method returns an <b>HRESULT</b> value. If the property call was not successful, it returns the appropriate <b>HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschematicket2.md">IPrintSchematicket2</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemaparameterinitializer.md">IPrintSchemaParameterInitializer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchematicket2::GetParameterInitializer method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
