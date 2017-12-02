---
UID: NF.prcomoem.IPrintOemUI.PublishDriverInterface
title: IPrintOemUI::PublishDriverInterface
author: windows-driver-content
description: The IPrintOemUI::PublishDriverInterface method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver's IPrintOemDriverUI, IPrintCoreUI2, IPrintCoreHelperPS, or IPrintCoreHelperUni interface.
old-location: print\iprintoemui_publishdriverinterface.htm
old-project: print
ms.assetid: 4c2053ec-c6b3-4584-b689-dc887610c57e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUI, PublishDriverInterface, IPrintOemUI::PublishDriverInterface
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
req.alt-api: IPrintOemUI.PublishDriverInterface
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
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::PublishDriverInterface method



## -description
<p>The <code>IPrintOemUI::PublishDriverInterface</code> method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver's <b>IPrintOemDriverUI</b>, <b>IPrintCoreUI2</b>, <b>IPrintCoreHelperPS</b>, or <b>IPrintCoreHelperUni</b> interface.</p>


## -syntax

````
HRESULT PublishDriverInterface(
   IUnknown *pIUnknown
);
````


## -parameters
<dl>

### -param pIUnknown 

<dd>
<p>Caller-supplied pointer to the <b>IUnknown</b> interface of the driver's <a href="https://msdn.microsoft.com/3c9df0ac-d823-4c27-bd34-85765f48b972">IPrintCoreUI2 COM Interface</a>, <a href="https://msdn.microsoft.com/ed11789f-750d-4f29-b5e0-ab299a1388db">IPrintOemDriverUI COM Interface</a>, <a href="print.iprintcorehelperps_interface">IPrintCoreHelperPS Interface</a>, or <a href="print.iprintcorehelperuni_interface">IPrintCoreHelperUni Interface</a>. See Remarks.</p>
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
<p>The Pscript5 driver supports the <b>IPrintCoreUI2</b>, <b>IPrintOemDriverUI</b>, and <b>IPrintCoreHelperPS</b> interfaces. Unidrv supports the <b>IPrintOemDriverUI</b> and <b>IPrintCoreHelperUni</b> interfaces. User interface plug-ins for both types of driver must implement the <code>IPrintOemUI::PublishDriverInterface</code> method.</p>

<p>The method should return information on its supported Pscript5 interfaces as follows:</p>

<p>The Pscript5 driver first calls the <code>IPrintOemUI::PublishDriverInterface</code> method with the <i>pIUnknown</i> pointer set to the <b>IPrintCoreUI2</b> instance's <b>IUnknown</b> interface. If the user interface plug-in is able to use the <b>IPrintCoreUI2</b> interface, the method must return S_OK. Otherwise, the plug-in should return E_FAIL.</p>

<p>If the plug-in has returned E_FAIL, the Pscript5 driver calls the <code>IPrintOemUI::PublishDriverInterface</code> method again, but with the <i>pIUnknown</i> pointer set to the <b>IPrintOemDriverUI</b> instance's <b>IUnknown</b> interface. If the plug-in can use the <b>IPrintOemDriverUI</b> interface, the method must return S_OK. Otherwise, the plug-in should return E_FAIL.</p>

<p>If the plug-in's <b>IPrintOemUI::GetInfo</b> method has returned a value of OEMPUBLISH_IPRINTCOREHELPER in <i>pBuffer</i> in response to a call with <i>dwMode</i> set to OEMGI_GETREQUESTEDHELPERINTERFACES, the Pscript5 driver calls the <code>IPrintOemUI::PublishDriverInterface</code> method again, but with the <i>pIUnknown</i> pointer set to an object that implements the <b>IPrintCoreHelperPS</b> and <b>IPrintCoreHelper</b> interfaces. If the plug-in can use the <b>IPrintCoreHelperPS</b> or <b>IPrintCoreHelper</b> interface, the method should return S_OK. Otherwise, the method should return E_FAIL.</p>

<p>The method should return information on its supported Unidrv interfaces as follows:</p>

<p>The Unidrv driver first calls the <code>IPrintOemUI::PublishDriverInterface</code> method with the <i>pIUnknown</i> pointer set to the <b>IPrintOemDriverUI</b> instance's <b>IUnknown</b> interface. If the plug-in is able to use the <b>IPrintOemDriverUI</b> interface, the method must return S_OK. Otherwise, the plug-in should return E_FAIL.</p>

<p>If the plug-in's <a href="print.iprintoemui_getinfo">IPrintOemUI::GetInfo</a> method has returned a value of OEMPUBLISH_IPRINTCOREHELPER in <i>pBuffer</i> in response to a call with <i>dwMode</i> set to OEMGI_GETREQUESTEDHELPERINTERFACES, the Unidrv driver calls the <code>IPrintOemUI::PublishDriverInterface</code> method again, but with the <i>pIUnknown</i> pointer set to an object that implements the <b>IPrintCoreHelperUni</b> and <b>IPrintCoreHelper</b> interfaces. If the plug-in uses the <b>IPrintCoreHelperUni</b> or <b>IPrintCoreHelper</b> interface, the method should return S_OK. Otherwise, the method should return E_FAIL.</p>

<p>If the plug-in fails all calls to <code>IPrintOemUI::PublishDriverInterface</code>, the plug-in will not receive further calls. If the user interface plug-in will be calling <b>IPrintCoreUI2</b>, <b>IPrintOemDriverUI</b>, <b>IPrintCoreHelperPS</b>, or <b>IPrintCoreHelperUni</b> interface methods, it must use the received <b>IUnknown</b> interface pointer to call <b>IUnknown::QueryInterface </b>(described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the <b>IPrintCoreUI2</b>, <b>IPrintOemDriverUI</b>, <b>IPrintCoreHelperPS</b>, or <b>IPrintCoreHelperUni</b> interface. For more information, see <a href="https://msdn.microsoft.com/8182cba5-4461-4ca0-8b01-342519609b1f">Interface Identifiers for Printer Drivers</a>.</p>

<p>During processing of each DDI function, UI plug-ins should not mix the use of methods of the pre-Windows Vista interfaces (for example, the <a href="print.iprintoemdriverui_interface">IPrintOemDriverUI</a> or <a href="print.iprintcoreui2_interface">IPrintCoreUI2</a> interface) and the new methods of the Windows Vista interfaces (for example, <a href="print.iprintcorehelperuni_interface">IPrintCoreHelperUni</a> or <a href="print.iprintcorehelperps_interface">IPrintCoreHelperPS</a>) to read or write driver settings. For example, during the <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> method, the UI plug-in should not use the <a href="print.iprintoemdriverui_drvupdateuisetting">IPrintOemDriverUI::DrvUpdateUISetting</a> method to write settings and use the <a href="print.iprintcorehelper_getoption">IPrintCoreHelper::GetOption</a> method to read settings. For another example, during the <a href="print.iprintoemui_printerevent">IPrintOemUI::PrinterEvent</a> method, the UI plug-in should not use the <a href="print.iprintcoreui2_getoptions">IPrintCoreUI2::GetOptions</a> method to read settings and use the <a href="print.iprintcorehelper_setoptions">IPrintCoreHelper::SetOptions</a> method to write settings. Synchronization of the reading and writing of settings is not supported between these different versions of interfaces.</p>

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
<a href="print.iprintoemui_getinfo">IPrintOemUI::GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::PublishDriverInterface method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
