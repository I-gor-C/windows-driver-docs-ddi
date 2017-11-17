---
UID: NF.prcomoem.IPrintOemUni.DevMode
title: IPrintOemUni::DevMode
author: windows-driver-content
description: The IPrintOemUni::DevMode method, provided by rendering plug-ins for Unidrv, performs operations on private DEVMODEW members.
old-location: print\iprintoemuni_devmode.htm
ms.assetid: df6bde70-ba14-411b-88a1-b45f2e2756ef
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
req.alt-api: IPrintOemUni.DevMode
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
ms.keywords: IPrintOemUni, DevMode, IPrintOemUni::DevMode
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::DevMode method



## -description
<p>The <code>IPrintOemUni::DevMode</code> method, provided by rendering plug-ins for Unidrv, performs operations on private <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> members.</p>


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
<p>Specifies a caller-supplied constant. See the Remarks section for more information.</p>
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
</dl><p>The operation failed</p>

<p> </p>

## -remarks
<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::DevMode</code> method.</p>

<p>If you are providing a user interface plug-in for Unidrv, and if you are adding private members to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure, you must implement both the <code>IPrintOemUI::DevMode</code> and the <code>IPrintOemUni::DevMode</code> methods. The code implementing these methods must be identical and can be placed in a library that is statically linked to both the UI plug-in and the rendering plug-in.</p>

<p>The <code>IPrintOemUni::DevMode</code> method must perform the operation indicated by its <i>dwMode</i> value. Each time <code>IPrintOemUni::DevMode</code> is called, <i>dwMode</i> contains one of the following constants, which are listed in the order they are received:</p>

<p></p><dl>
<dt><a id="OEMDM_SIZE"></a><a id="oemdm_size"></a>OEMDM_SIZE</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should return the size of the memory allocation needed to store the render plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>
<p>The printer driver DLL allocates the specified amount of memory and passes its address to the rendering plug-in in subsequent calls to <code>IPrintOemUni::DevMode</code>.</p>
</dd>
<dt><a id="OEMDM_DEFAULT"></a><a id="oemdm_default"></a>OEMDM_DEFAULT</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>
</dd>
<dt><a id="OEMDM_CONVERT"></a><a id="oemdm_convert"></a>OEMDM_CONVERT</dt>
<dd>
<p>Indicates the <code>IPrintOemUni::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>
<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUni::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>
</dd>
<dt><a id="OEMDM_MERGE"></a><a id="oemdm_merge"></a>OEMDM_MERGE</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>
<ul>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>
</li>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>
</li>
</ul>
<p>The method should validate the contents of each private DEVMODEW member pointed to by <i>pOEMDMIn</i>. Each valid value should be copied to the output buffer pointed to by <i>pOEMDMOut</i>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>
</dd>
</dl><p>Indicates that the <code>IPrintOemUni::DevMode</code> method should return the size of the memory allocation needed to store the render plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>

<p>The printer driver DLL allocates the specified amount of memory and passes its address to the rendering plug-in in subsequent calls to <code>IPrintOemUni::DevMode</code>.</p>

<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>

<p>Indicates the <code>IPrintOemUni::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUni::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>

<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>

<p>The method should validate the contents of each private DEVMODEW member pointed to by <i>pOEMDMIn</i>. Each valid value should be copied to the output buffer pointed to by <i>pOEMDMOut</i>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>

<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::DevMode</code> method.</p>

<p>If you are providing a user interface plug-in for Unidrv, and if you are adding private members to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure, you must implement both the <code>IPrintOemUI::DevMode</code> and the <code>IPrintOemUni::DevMode</code> methods. The code implementing these methods must be identical and can be placed in a library that is statically linked to both the UI plug-in and the rendering plug-in.</p>

<p>The <code>IPrintOemUni::DevMode</code> method must perform the operation indicated by its <i>dwMode</i> value. Each time <code>IPrintOemUni::DevMode</code> is called, <i>dwMode</i> contains one of the following constants, which are listed in the order they are received:</p>

<p></p><dl>
<dt><a id="OEMDM_SIZE"></a><a id="oemdm_size"></a>OEMDM_SIZE</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should return the size of the memory allocation needed to store the render plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>
<p>The printer driver DLL allocates the specified amount of memory and passes its address to the rendering plug-in in subsequent calls to <code>IPrintOemUni::DevMode</code>.</p>
</dd>
<dt><a id="OEMDM_DEFAULT"></a><a id="oemdm_default"></a>OEMDM_DEFAULT</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>
</dd>
<dt><a id="OEMDM_CONVERT"></a><a id="oemdm_convert"></a>OEMDM_CONVERT</dt>
<dd>
<p>Indicates the <code>IPrintOemUni::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>
<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUni::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>
</dd>
<dt><a id="OEMDM_MERGE"></a><a id="oemdm_merge"></a>OEMDM_MERGE</dt>
<dd>
<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>
<ul>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>
</li>
<li>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>
</li>
</ul>
<p>The method should validate the contents of each private DEVMODEW member pointed to by <i>pOEMDMIn</i>. Each valid value should be copied to the output buffer pointed to by <i>pOEMDMOut</i>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>
</dd>
</dl><p>Indicates that the <code>IPrintOemUni::DevMode</code> method should return the size of the memory allocation needed to store the render plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>cbBufSize</b> member.</p>

<p>The printer driver DLL allocates the specified amount of memory and passes its address to the rendering plug-in in subsequent calls to <code>IPrintOemUni::DevMode</code>.</p>

<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should fill the private DEVMODEW members with their default values. For this operation, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the <b>pOEMDMOut</b> member, and return the number of bytes written by placing it in the <b>cbBufSize</b> member.</p>

<p>Indicates the <code>IPrintOemUni::DevMode</code> method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559588">OEM_DMEXTRAHEADER</a> structure.</p>

<p>The public and private members of the DEVMODEW structure to be converted are pointed to by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members. The <code>IPrintOemUni::DevMode</code> method should place converted private members in the memory space described by the structure's <b>pOEMDMOut</b> and <b>cbBufSize</b> members, and it should return the count of written bytes by placing it in the structure's <b>cbBufSize</b> member. The value returned in <b>cbBufSize</b> cannot be larger than the value received.</p>

<p>Indicates that the <code>IPrintOemUni::DevMode</code> method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMIn</b> and <b>pOEMDMIn</b> members point to the public and private members of the DEVMODEW structure to be validated.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557686">OEMDMPARAM</a> structure's <b>pPublicDMOut</b> and <b>pOEMDMOut</b> members point to current default DEVMODEW values (obtained from property sheet contents).</p>

<p>The method should validate the contents of each private DEVMODEW member pointed to by <i>pOEMDMIn</i>. Each valid value should be copied to the output buffer pointed to by <i>pOEMDMOut</i>, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S_OK.)</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554167">IPrintOemUI::DevMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni::DevMode method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
