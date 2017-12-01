---
UID: NF.printerextension.IPrintSchemaTicket.GetFeatureByKeyName
title: IPrintSchemaTicket::GetFeatureByKeyName
author: windows-driver-content
description: Gets a feature from the PrintTicket based on the specified key name.
old-location: print\iprintschematicket_getfeaturebykeyname.htm
old-project: print
ms.assetid: 3BD7B8D6-B06F-492F-A73E-DA0799387B2A
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket, GetFeatureByKeyName, IPrintSchemaTicket::GetFeatureByKeyName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintSchemaTicket.GetFeatureByKeyName
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
req.iface: IPrintSchemaTicket
req.product: Windows 10 or later.
---

# IPrintSchemaTicket::GetFeatureByKeyName method



## -description
<p>Gets a feature from the PrintTicket based on the specified key name.</p>


## -syntax

````
HRESULT GetFeatureByKeyName(
  [in]          BSTR                bstrKeyName,
  [out, retval] IPrintSchemaFeature **ppFeature
);
````


## -parameters
<dl>

### -param <i>bstrKeyName</i> [in]

<dd>
<p>The key name of the feature.</p>
</dd>

### -param <i>ppFeature</i> [out, retval]

<dd>
<p>The returned feature.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

## -remarks
<p>See <a href="print.iprintschemacapabilities_getfeaturebykeyname">IPrintSchemaCapabilities::GetFeatureByKeyName</a> for the recognized feature key names, the key names’ equivalent public Print Schema feature names, and the supported specialized option types.</p>

<p>When the requested feature, option or property is not found, this method returns S_FALSE and sets a NULL pointer on the output object of the feature, option or property.</p>

<p>So if the <a href="..\printerextension\nn-printerextension-iprintschematicket.md">IPrintSchemaTicket</a> object does not contain the specified feature, option or property, the app must obtain an <a href="..\printerextension\nn-printerextension-iprintschemacapabilities.md">IPrintSchemaCapabilities</a> object and query it via <b>IPrintSchemaCapabilities::GetFeatureByKeyName</b> or via <a href="print.iprintschemacapabilities_getfeature">IPrintSchemaCapabilities::GetFeature</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Windows 8</p>
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
<a href="..\printerextension\nn-printerextension-iprintschematicket.md">IPrintSchemaTicket</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemacapabilities.md">IPrintSchemaCapabilities</a>
</dt>
<dt>
<a href="print.iprintschemacapabilities_getfeature">IPrintSchemaCapabilities::GetFeature</a>
</dt>
<dt>
<a href="print.iprintschemacapabilities_getfeaturebykeyname">IPrintSchemaCapabilities::GetFeatureByKeyName</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprintschemafeature.md">IPrintSchemaFeature</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaTicket::GetFeatureByKeyName method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
