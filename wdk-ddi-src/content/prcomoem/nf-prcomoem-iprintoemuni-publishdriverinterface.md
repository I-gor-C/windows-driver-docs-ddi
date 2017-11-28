---
UID: NF.prcomoem.IPrintOemUni.PublishDriverInterface
title: IPrintOemUni::PublishDriverInterface
author: windows-driver-content
description: The IPrintOemUni::PublishDriverInterface method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's IPrintOemDriverUni or IPrintCoreHelperUni interface.
old-location: print\iprintoemuni_publishdriverinterface.htm
old-project: print
ms.assetid: 72bfa383-a7f2-4aa6-a45c-564928705e42
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, PublishDriverInterface, IPrintOemUni::PublishDriverInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUni.PublishDriverInterface
req.alt-loc: prcomoem.h
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
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::PublishDriverInterface method



## -description
<p>The <code>IPrintOemUni::PublishDriverInterface</code> method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's <b>IPrintOemDriverUni</b> or <b>IPrintCoreHelperUni</b> interface.</p>


## -syntax

````
HRESULT PublishDriverInterface(
   IUnknown *pIUnknown
);
````


## -parameters
<dl>

### -param <i>pIUnknown</i> 

<dd>
<p>Caller-supplied pointer to the <b>IUnknown</b> interface of the driver's <a href="NULL">IPrintOemDriverUni COM Interface</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff552940">IPrintCoreHelperUni interface</a>.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p>

<p> </p>

## -remarks
<p>A rendering plug-in for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> must implement the <code>IPrintOemUni::PublishDriverInterface</code> method, and the method must return S_OK in response to at least one call. Otherwise, the driver will not call the plug-in's other <b>IPrintOemUni</b> interface methods.</p>

<p>The method should return information on its supported Unidrv interfaces as follows:</p>

<p>The Unidrv driver first calls the <code>IPrintOemUI::PublishDriverInterface</code> method with the <i>pIUnknown</i> pointer set to the <b>IPrintOemDriverUni</b> instance's <b>IUnknown</b> interface. If the rendering plug-in will be calling <b>IPrintOemDriverUni</b> interface methods, it must use the received <b>IUnknown</b> interface pointer to call <b>IUnknown::QueryInterface </b>(described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the <b>IPrintOemDriverUni</b> interface. For more information, see <a href="NULL">Interface Identifiers for Printer Drivers</a>.</p>

<p>If the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554256">IPrintOemUni::GetInfo</a> method has returned a value of OEMPUBLISH_IPRINTCOREHELPER in <i>pBuffer</i> in response to a call with <i>dwMode</i> set to OEMGI_GETREQUESTEDHELPERINTERFACES, the Unidrv driver calls the <code>IPrintOemUni::PublishDriverInterface</code> method again, but with the <i>pIUnknown</i> pointer set to an object that implements the <b>IPrintCoreHelperUni</b> and <b>IPrintCoreHelper</b> interfaces. If the plug-in retains a pointer to the object, the method should return S_OK. Otherwise, the method should return E_FAIL.</p>

<p>A rendering plug-in for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> must implement the <code>IPrintOemUni::PublishDriverInterface</code> method, and the method must return S_OK in response to at least one call. Otherwise, the driver will not call the plug-in's other <b>IPrintOemUni</b> interface methods.</p>

<p>The method should return information on its supported Unidrv interfaces as follows:</p>

<p>The Unidrv driver first calls the <code>IPrintOemUI::PublishDriverInterface</code> method with the <i>pIUnknown</i> pointer set to the <b>IPrintOemDriverUni</b> instance's <b>IUnknown</b> interface. If the rendering plug-in will be calling <b>IPrintOemDriverUni</b> interface methods, it must use the received <b>IUnknown</b> interface pointer to call <b>IUnknown::QueryInterface </b>(described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the <b>IPrintOemDriverUni</b> interface. For more information, see <a href="NULL">Interface Identifiers for Printer Drivers</a>.</p>

<p>If the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554256">IPrintOemUni::GetInfo</a> method has returned a value of OEMPUBLISH_IPRINTCOREHELPER in <i>pBuffer</i> in response to a call with <i>dwMode</i> set to OEMGI_GETREQUESTEDHELPERINTERFACES, the Unidrv driver calls the <code>IPrintOemUni::PublishDriverInterface</code> method again, but with the <i>pIUnknown</i> pointer set to an object that implements the <b>IPrintCoreHelperUni</b> and <b>IPrintCoreHelper</b> interfaces. If the plug-in retains a pointer to the object, the method should return S_OK. Otherwise, the method should return E_FAIL.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554256">IPrintOemUni::GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni::PublishDriverInterface method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
