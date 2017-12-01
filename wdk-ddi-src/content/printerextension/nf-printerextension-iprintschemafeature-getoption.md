---
UID: NF.printerextension.IPrintSchemaFeature.GetOption
title: IPrintSchemaFeature::GetOption
author: windows-driver-content
description: Gets the option with the given name.
old-location: print\iprintschemafeature_getoption.htm
old-project: print
ms.assetid: C9C4E085-1F2A-4610-AF2A-8F87E5CE7BCA
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaFeature, GetOption, IPrintSchemaFeature::GetOption
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
req.alt-api: IPrintSchemaFeature.GetOption
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
req.iface: IPrintSchemaFeature
req.product: Windows 10 or later.
---

# IPrintSchemaFeature::GetOption method



## -description
<p>Gets the option with the given name.</p>


## -syntax

````
HRESULT GetOption(
  [in]          BSTR               bstrName,
  [in]          BSTR               bstrNamespaceUri = PRINTSCHEMA_KEYWORDS_NAMESPACE_URI,
  [out, retval] IPrintSchemaOption **ppOption
);
````


## -parameters
<dl>

### -param <i>bstrName</i> [in]

<dd>
<p>The name of the option.</p>
</dd>

### -param <i>bstrNamespaceUri</i> [in]

<dd>
<p>The namespace URI of the option.</p>
</dd>

### -param <i>ppOption</i> [out, retval]

<dd>
<p>The returned option.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value, if the call was successful. Otherwise it returns the appropriate error code.</p>

## -remarks
<p>When the requested feature, option or property is not found, this method returns S_FALSE and sets a NULL pointer on the output object of the feature, option or property.</p>

<p>So if the <a href="..\printerextension\nn-printerextension-iprintschematicket.md">IPrintSchemaTicket</a> object does not contain the specified feature, option or property, the app must obtain an <a href="..\printerextension\nn-printerextension-iprintschemacapabilities.md">IPrintSchemaCapabilities</a> object and query it via <a href="print.iprintschemacapabilities_getfeaturebykeyname">IPrintSchemaCapabilities::GetFeatureByKeyName</a> or via <a href="print.iprintschemacapabilities_getfeature">IPrintSchemaCapabilities::GetFeature</a>.</p>

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
<a href="..\printerextension\nn-printerextension-iprintschemacapabilities.md">IPrintSchemaCapabilities</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemafeature.md">IPrintSchemaFeature</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschematicket.md">IPrintSchemaTicket</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemaoption.md">IPrintSchemaOption</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaFeature::GetOption method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
