---
UID: NF.prcomoem.IPrintCoreHelper.CreateInstanceOfMSXMLObject
title: IPrintCoreHelper::CreateInstanceOfMSXMLObject
author: windows-driver-content
description: The IPrintCoreHelper::CreateInstanceOfMSXMLObject method creates an instance of an MSXML 6.0 object by using the correct MSXML DLL.
old-location: print\iprintcorehelper_createinstanceofmsxmlobject.htm
ms.assetid: d4b91262-f349-4824-bab0-5e3725a81cb3
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
req.alt-api: IPrintCoreHelper.CreateInstanceOfMSXMLObject
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
ms.keywords: IPrintCoreHelper, CreateInstanceOfMSXMLObject, IPrintCoreHelper::CreateInstanceOfMSXMLObject
req.iface: IPrintCoreHelper
req.product: Windows 10 or later.
---

# IPrintCoreHelper::CreateInstanceOfMSXMLObject method



## -description
<p>The <b>IPrintCoreHelper::CreateInstanceOfMSXMLObject</b> method creates an instance of an MSXML 6.0 object by using the correct MSXML DLL. </p>


## -syntax

````
HRESULT CreateInstanceOfMSXMLObject(
  [in]  REFCLSID  rclsid,
  [in]  LPUNKNOWN pUnkOuter,
  [in]  DWORD     dwClsContext,
  [in]  REFIID    riid,
  [out] LPVOID    *ppv
);
````


## -parameters
<dl>

### -param <i>rclsid</i> [in]

<dd>
<p>The CLSID that is associated with the data and code that will be used to create the object. </p>
</dd>

### -param <i>pUnkOuter</i> [in]

<dd>
<p>A pointer to the aggregate object's <b>IUnknown</b> interface (the controlling <b>IUnknown</b>). This parameter must be <b>NULL</b>, which means that the object is not being created as part of an aggregate. </p>
</dd>

### -param <i>dwClsContext</i> [in]

<dd>
<p>The context in which the code that manages the newly created object will run. The only valid values are <b>NULL</b> and CLSCTX_INPROC_SERVER, which is a value of the CLSCTX enumeration (described in the Microsoft Windows SDK documentation).</p>
</dd>

### -param <i>riid</i> [in]

<dd>
<p>A reference to the identifier of the interface that will be used to communicate with the object. </p>
</dd>

### -param <i>ppv</i> [out]

<dd>
<p>A pointer to a variable that receives the address of the interface that is requested in the <i>riid</i> parameter. If <b>IPrintCoreHelper::CreateInstanceOfMSXMLObject</b> successfully returns, *<i>ppv</i> contains the address of the requested interface. If this method fails, *<i>ppv</i> contains <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>IPrintCoreHelper::CreateInstanceOfMSXMLObject</b> should return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>An instance of the specified object class was successfully created.</p><dl>
<dt><b>CLASS_E_NOAGGREGATION</b></dt>
</dl><p>The specified class cannot be created as part of an aggregate.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The specified class does not implement the requested interface, or the controlling <b>IUnknown</b> interface does not expose the requested interface.</p><dl>
<dt><b>REGDB_E_CLASSNOTREG</b></dt>
</dl><p>A specified class is not registered in the registration database. This value can also indicate that the type of server you requested in the CLSCTX enumeration type is not registered or the values for the server types in the registry are corrupt.</p>

<p> </p>

## -remarks
<p><b>IPrintCoreHelper::CreateInstanceOfMSXMLObject</b> enables a plug-in to use MSXML objects safely even when it runs on down-level client machines (that is, client machines that run Windows Server 2003, Windows XP, or Windows 2000). </p>

<p>The parameters in this method map directly to those of the <b>CoCreateInstance</b> function (which is described in the Windows SDK documentation). Note that installing a Windows Vista driver on a machine that runs a previous version of Windows does not cause MSXML 6.0 to be installed. The actual DLL is included with the driver-dependent DLLs and is loaded from the driver directory. It is not registered on the system. Plug-ins that use this method should create only MSXML objects.</p>

<p><b>IPrintCoreHelper::CreateInstanceOfMSXMLObject</b> enables a plug-in to use MSXML objects safely even when it runs on down-level client machines (that is, client machines that run Windows Server 2003, Windows XP, or Windows 2000). </p>

<p>The parameters in this method map directly to those of the <b>CoCreateInstance</b> function (which is described in the Windows SDK documentation). Note that installing a Windows Vista driver on a machine that runs a previous version of Windows does not cause MSXML 6.0 to be installed. The actual DLL is included with the driver-dependent DLLs and is loaded from the driver directory. It is not registered on the system. Plug-ins that use this method should create only MSXML objects.</p>

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