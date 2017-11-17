---
UID: NF.prcomoem.IPrintCoreHelperPS.CreateInstanceOfMSXMLObject
title: IPrintCoreHelperPS::CreateInstanceOfMSXMLObject
author: windows-driver-content
description: The IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method creates an instance of an MSXML object.
old-location: print\iprintcorehelperps_createinstanceofmsxmlobject.htm
ms.assetid: 017f6e00-694b-4ada-86be-cf2be047fa88
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
req.alt-api: IPrintCoreHelperPS.CreateInstanceOfMSXMLObject
req.alt-loc: Prcomoem.h
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
ms.keywords: IPrintCoreHelperPS, CreateInstanceOfMSXMLObject, IPrintCoreHelperPS::CreateInstanceOfMSXMLObject
req.iface: IPrintCoreHelperPS
req.product: Windows 10 or later.
---

# IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method



## -description
<p>The <b>IPrintCoreHelperPS::CreateInstanceOfMSXMLObject</b> method creates an instance of an MSXML object. </p>


## -syntax

````
STDMETHOD CreateInstanceOfMSXMLObject(
  [in]  REFCLSID  rclsid,
  [in]  LPUNKNOWN pUnkOuter,
  [in]  DWORD     dwClsContext,
  [in]  REFIID    riid,
  [out] LPVOID    ppv
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
<p>A pointer to a memory address that receives the address of the interface that is requested in the <i>riid</i> parameter. If <b>IPrintCoreHelperPS::CreateInstanceOfMSXMLObject</b> successfully returns, *<i>ppv</i> contains the address of the requested interface. If this method fails, *<i>ppv</i> contains <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>IPrintCoreHelperPS::CreateInstanceOfMSXMLObject</b> should return one of the following values.</p><dl>
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
<p>The plug-in should not directly create an MSXML object by calling CoCreateInstance (described in the Windows SDK documentation). Instead, it should call Pscript to do so. The reason is that under certain conditions in which the printer driver might be used, such as with older operating system versions, the operating system does not need to register the required version of MSXML, which currently is version 6. In such situations, calling CoCreateInstance can fail. However, the core driver ensures that wherever the driver is present, the MSXML parser DLL is also present on the machine, making it possible to create an MSXML object when needed.</p>

<p>The plug-in should not directly create an MSXML object by calling CoCreateInstance (described in the Windows SDK documentation). Instead, it should call Pscript to do so. The reason is that under certain conditions in which the printer driver might be used, such as with older operating system versions, the operating system does not need to register the required version of MSXML, which currently is version 6. In such situations, calling CoCreateInstance can fail. However, the core driver ensures that wherever the driver is present, the MSXML parser DLL is also present on the machine, making it possible to create an MSXML object when needed.</p>

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