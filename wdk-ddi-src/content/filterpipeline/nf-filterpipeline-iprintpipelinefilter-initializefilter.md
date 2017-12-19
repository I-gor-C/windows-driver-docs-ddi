---
UID: NF.filterpipeline.IPrintPipelineFilter.InitializeFilter
title: IPrintPipelineFilter::InitializeFilter method
author: windows-driver-content
description: The InitializeFilter method initializes a filter.
old-location: print\iprintpipelinefilter_initializefilter.htm
old-project: print
ms.assetid: a28a8ee0-24df-45b5-8850-f3b3984b3b64
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IPrintPipelineFilter, IPrintPipelineFilter::InitializeFilter, InitializeFilter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintPipelineFilter.InitializeFilter
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# IPrintPipelineFilter::InitializeFilter method



## -description
The <code>InitializeFilter</code> method initializes a filter.



## -syntax

````
HRESULT InitializeFilter(
  [in] IInterFilterCommunicator     *pICommunicator,
  [in] IPrintPipelinePropertyBag    *pIPropertyBag,
  [in] IPrintPipelineManagerControl *pIPipelineControl
);
````


## -parameters

### -param pICommunicator [in]

A pointer to the <a href="print.iinterfiltercommunicator">IInterFilterCommunicator</a> interface.


### -param pIPropertyBag [in]

A pointer to the<a href="print.iprintpipelinepropertybag">IPrintPipelinePropertyBag</a> interface.


### -param pIPipelineControl [in]

A pointer to the <a href="print.iprintpipelinemanagercontrol">IPrintPipelineManagerControl</a> interface.


## -returns
<code>InitializeFilter</code> returns an <b>HRESULT</b> value. The method should return a value other than "S_OK" or "S_FALSE" if the necessary operations are not performed inside <code>InitializeFilter</code>.


## -remarks
When the <code>InitializeFilter</code> method is called, the filters should:

Get, add, or delete properties from the property bag.

Get the read and write interfaces.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IDL

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iinterfiltercommunicator">IInterFilterCommunicator</a>
</dt>
<dt>
<a href="print.iprintpipelinemanagercontrol">IPrintPipelineManagerControl</a>
</dt>
<dt>
<a href="print.iprintpipelinepropertybag">IPrintPipelinePropertyBag</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintPipelineFilter::InitializeFilter method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

