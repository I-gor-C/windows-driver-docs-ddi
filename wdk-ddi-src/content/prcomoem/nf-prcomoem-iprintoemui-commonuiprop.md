---
UID: NF.prcomoem.IPrintOemUI.CommonUIProp
title: IPrintOemUI::CommonUIProp
author: windows-driver-content
description: The IPrintOemUI::CommonUIProp method allows a user interface plug-in to modify an existing printer property sheet page.
old-location: print\iprintoemui_commonuiprop.htm
ms.assetid: 6218913c-d11c-4646-a292-5f8740097d58
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUI.CommonUIProp
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
ms.keywords: IPrintOemUI, CommonUIProp, IPrintOemUI::CommonUIProp
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::CommonUIProp method



## -description
<p>The <code>IPrintOemUI::CommonUIProp</code> method allows a user interface plug-in to modify an existing printer property sheet page.</p>


## -syntax

````
HRESULT CommonUIProp(
   DWORD         dwMode,
   POEMCUIPPARAM pOemCUIPParam
);
````


## -parameters
<dl>

### -param <i>dwMode</i> 

<dd>
<p>Caller-supplied integer constant indicating which property sheet page should be modified. The following constants are valid.</p>
<table>
<tr>
<th>Value</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>OEMCUIP_DOCPROP</p>
</td>
<td>
<p>The method is being called to modify the Layout, Paper/Quality, or Advanced page of the document property sheet.</p>
</td>
</tr>
<tr>
<td>
<p>OEMCUIP_PRNPROP</p>
</td>
<td>
<p>The method is being called to modify the Device Settings page of the printer property sheet.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pOemCUIPParam</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557653">OEMCUIPPARAM</a> structure.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>When a user interface plug-in's <code>IPrintOemUI::CommonUIProp</code> method is called, it should return customized property sheet option items in order to modify an existing printer property sheet page.</p>

<p>The <code>IPrintOemUI::CommonUIProp</code> method is called by the printer driver's <a href="NULL">printer interface DLL</a>. The method should supply an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structures describing property sheet items, along with a callback function for processing user modifications to option values.</p>

<p>You should expect the method to be called twice for each property sheet. The method's <i>dwMode</i> parameter value indicates whether it is being called to make changes to the printer property sheet or the document property sheet.</p>

<p>The first time it is called, the method should just return the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structures to be added. This number should be placed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557653">OEMCUIPPARAM</a> structure's <b>cOEMOptItems</b> member. The printer interface DLL then allocates enough memory to store the specified number of OPTITEMs, and calls <code>IPrintOemUI::CommonUIProp</code> again.</p>

<p>The second time it is called, the <code>IPrintOemUI::CommonUIProp</code> method should do the following:</p>

<p>Fill the driver-supplied array of OPTITEM structures with option descriptions. This array is pointed to by the OEMCUIPPARAM structure's <b>pOEMOptItems</b> member, and the number of allocated array elements is contained in the structure's <b>cOEMOptItems</b> member. (For information about specifying OPTITEM member values, see the description of the OEMCUIPPARAM structure's <b>pOEMOptItems</b> member).</p>

<p>Return the number of structures added to the OPTITEM array by placing the number in the OEMCUIPPARAM structure's <b>cOEMOptItems</b> member.</p>

<p>Return the address of a callback function in the OEMCUIPPARAM structure's <b>OEMCUIPCallback</b> member. This callback function is called when a user modifies the property sheet page. The callback function must be of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557650">OEMCUIPCALLBACK</a>.</p>

<p>Optionally, return the address of a private data structure by placing it in the OEMCUIPPARAM structure's <b>pOEMUserData</b> member. The callback function specified by the structure's <b>OEMCUIPCallback</b> member receives the OEMCUIPPARAM structure's address as an input parameter and can therefore obtain the private data's address.</p>

<p>Space for the private data structure should be allocated by calling the Microsoft Windows SDK <b>HeapAlloc</b> function, using the handle contained in the OEMCUIPPARAM structure's <b>hOEMHeap</b> member.</p>

<p>If <code>IPrintOemUI::CommonUIProp</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information, see <a href="NULL">Modifying a Driver-Supplied Property Sheet Page</a>.</p>

<p>When a user interface plug-in's <code>IPrintOemUI::CommonUIProp</code> method is called, it should return customized property sheet option items in order to modify an existing printer property sheet page.</p>

<p>The <code>IPrintOemUI::CommonUIProp</code> method is called by the printer driver's <a href="NULL">printer interface DLL</a>. The method should supply an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structures describing property sheet items, along with a callback function for processing user modifications to option values.</p>

<p>You should expect the method to be called twice for each property sheet. The method's <i>dwMode</i> parameter value indicates whether it is being called to make changes to the printer property sheet or the document property sheet.</p>

<p>The first time it is called, the method should just return the number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structures to be added. This number should be placed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557653">OEMCUIPPARAM</a> structure's <b>cOEMOptItems</b> member. The printer interface DLL then allocates enough memory to store the specified number of OPTITEMs, and calls <code>IPrintOemUI::CommonUIProp</code> again.</p>

<p>The second time it is called, the <code>IPrintOemUI::CommonUIProp</code> method should do the following:</p>

<p>Fill the driver-supplied array of OPTITEM structures with option descriptions. This array is pointed to by the OEMCUIPPARAM structure's <b>pOEMOptItems</b> member, and the number of allocated array elements is contained in the structure's <b>cOEMOptItems</b> member. (For information about specifying OPTITEM member values, see the description of the OEMCUIPPARAM structure's <b>pOEMOptItems</b> member).</p>

<p>Return the number of structures added to the OPTITEM array by placing the number in the OEMCUIPPARAM structure's <b>cOEMOptItems</b> member.</p>

<p>Return the address of a callback function in the OEMCUIPPARAM structure's <b>OEMCUIPCallback</b> member. This callback function is called when a user modifies the property sheet page. The callback function must be of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557650">OEMCUIPCALLBACK</a>.</p>

<p>Optionally, return the address of a private data structure by placing it in the OEMCUIPPARAM structure's <b>pOEMUserData</b> member. The callback function specified by the structure's <b>OEMCUIPCallback</b> member receives the OEMCUIPPARAM structure's address as an input parameter and can therefore obtain the private data's address.</p>

<p>Space for the private data structure should be allocated by calling the Microsoft Windows SDK <b>HeapAlloc</b> function, using the handle contained in the OEMCUIPPARAM structure's <b>hOEMHeap</b> member.</p>

<p>If <code>IPrintOemUI::CommonUIProp</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information, see <a href="NULL">Modifying a Driver-Supplied Property Sheet Page</a>.</p>

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