---
UID: NF.wudfddi.IPnpCallbackSelfManagedIo.OnSelfManagedIoStop
title: IPnpCallbackSelfManagedIo::OnSelfManagedIoStop
author: windows-driver-content
description: The OnSelfManagedIoStop method is not used in the current version of the UMDF.
old-location: wdf\ipnpcallbackselfmanagedio_onselfmanagediostop.htm
old-project: wdf
ms.assetid: 490c95f5-ea93-4521-8fa5-4ca1f83ff19d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IPnpCallbackSelfManagedIo, OnSelfManagedIoStop, IPnpCallbackSelfManagedIo::OnSelfManagedIoStop
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPnpCallbackSelfManagedIo.OnSelfManagedIoStop
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IPnpCallbackSelfManagedIo
req.product: Windows 10 or later.
---

# IPnpCallbackSelfManagedIo::OnSelfManagedIoStop method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnSelfManagedIoStop</b> method is not used in the current version of the UMDF.</p>


## -syntax

````
HRESULT OnSelfManagedIoStop(
  [in] IWDFDevice *pWdfDevice
);
````


## -parameters
<dl>

### -param <i>pWdfDevice</i> [in]

<dd></dd>
</dl>

## -returns
<p>This method is not currently used.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>