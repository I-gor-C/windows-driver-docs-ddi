---
UID: NF.prcomoem.IPrintOemUI.DevMode
title: IPrintOemUI::DevMode
author: windows-driver-content
description: The IPrintOemUI::DevMode method, provided by user interface plug-ins, performs operations on the plug-in's private DEVMODEW members.
old-location: print\iprintoemui_devmode.htm
ms.assetid: decc76c4-1973-41c5-9091-6dc5b9ccd30d
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
req.alt-api: IPrintOemUI.DevMode
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
ms.keywords: IPrintOemUI, DevMode, IPrintOemUI::DevMode
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::DevMode method



## -description
<p>The <code>IPrintOemUI::DevMode</code> method, provided by user interface plug-ins, performs operations on the plug-in's private DEVMODEW members.</p>


## -syntax

````
STDMETHOD DevMode(
   DWORD       dwMode,
   POEMDMPARAM pOemDMParam
);
````


## -parameters
<dl>

### -param <i>dwMode</i> 

<dd>
<p>Caller-supplied constant. See the following Remarks section.</p>
</dd>

### -param <i>pOemDMParam</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure.</p>
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
<p>User interface plug-ins must implement a <code>IPrintOemUI::DevMode</code> method if they define private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure members. The method's purpose is to define, validate, or convert (from one version to another) the contents of the private DEVMODEW structure members.</p>

<p>A private DEVMODEW section must be prefaced by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The <code>IPrintOemUI::DevMode</code> method must perform the operation indicated by its <i>dwMode</i> value. Each time <code>IPrintOemUI::DevMode</code> is called, <i>dwMode</i> contains one of the following constants, which are listed in the order they are received:</p>

<p></p><dl>
<dt><a id="OEMDM_SIZE"></a><a id="oemdm_size"></a>OEMDM_SIZE</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should return the size of the memory allocation needed to store the user interface plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>
<p>The printer interface DLL allocates the specified amount of memory and passes its address to the user interface plug-in in subsequent calls to <code>IPrintOemUI::DevMode</code>.</p>
</dd>
<dt><a id="OEMDM_DEFAULT"></a><a id="oemdm_default"></a>OEMDM_DEFAULT</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>
</dd>
<dt><a id="OEMDM_CONVERT"></a><a id="oemdm_convert"></a>OEMDM_CONVERT</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>
<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUI::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>
</dd>
<dt><a id="OEMDM_MERGE"></a><a id="oemdm_merge"></a>OEMDM_MERGE</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>
<ul>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>
</li>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>
</li>
</ul>
<p>The method should validate the contents of each private DEVMODEW member pointed to by <b>pOEMDMIn</b>. Each valid value should be copied to the output buffer pointed to by <b>pOEMDMOut</b>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>
</dd>
</dl><p>Indicates the <code>IPrintOemUI::DevMode</code> method should return the size of the memory allocation needed to store the user interface plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>

<p>The printer interface DLL allocates the specified amount of memory and passes its address to the user interface plug-in in subsequent calls to <code>IPrintOemUI::DevMode</code>.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUI::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>

<p>The method should validate the contents of each private DEVMODEW member pointed to by <b>pOEMDMIn</b>. Each valid value should be copied to the output buffer pointed to by <b>pOEMDMOut</b>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>

<p>User interface plug-ins must implement a <code>IPrintOemUI::DevMode</code> method if they define private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure members. The method's purpose is to define, validate, or convert (from one version to another) the contents of the private DEVMODEW structure members.</p>

<p>A private DEVMODEW section must be prefaced by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The <code>IPrintOemUI::DevMode</code> method must perform the operation indicated by its <i>dwMode</i> value. Each time <code>IPrintOemUI::DevMode</code> is called, <i>dwMode</i> contains one of the following constants, which are listed in the order they are received:</p>

<p></p><dl>
<dt><a id="OEMDM_SIZE"></a><a id="oemdm_size"></a>OEMDM_SIZE</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should return the size of the memory allocation needed to store the user interface plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>
<p>The printer interface DLL allocates the specified amount of memory and passes its address to the user interface plug-in in subsequent calls to <code>IPrintOemUI::DevMode</code>.</p>
</dd>
<dt><a id="OEMDM_DEFAULT"></a><a id="oemdm_default"></a>OEMDM_DEFAULT</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>
</dd>
<dt><a id="OEMDM_CONVERT"></a><a id="oemdm_convert"></a>OEMDM_CONVERT</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>
<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUI::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>
</dd>
<dt><a id="OEMDM_MERGE"></a><a id="oemdm_merge"></a>OEMDM_MERGE</dt>
<dd>
<p>Indicates the <code>IPrintOemUI::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>
<ul>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>
</li>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>
</li>
</ul>
<p>The method should validate the contents of each private DEVMODEW member pointed to by <b>pOEMDMIn</b>. Each valid value should be copied to the output buffer pointed to by <b>pOEMDMOut</b>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>
</dd>
</dl><p>Indicates the <code>IPrintOemUI::DevMode</code> method should return the size of the memory allocation needed to store the user interface plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>

<p>The printer interface DLL allocates the specified amount of memory and passes its address to the user interface plug-in in subsequent calls to <code>IPrintOemUI::DevMode</code>.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUI::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>

<p>Indicates the <code>IPrintOemUI::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>

<p>The method should validate the contents of each private DEVMODEW member pointed to by <b>pOEMDMIn</b>. Each valid value should be copied to the output buffer pointed to by <b>pOEMDMOut</b>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554230">IPrintOemUni::DevMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553205">IPrintOemPS::DevMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::DevMode method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
