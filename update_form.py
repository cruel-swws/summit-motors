import re

html_content = """
                    <!-- Customer Information -->
                    <div>
                        <h3 class="text-xl font-bold leading-6 text-[#0f172a] mb-2 flex items-center gap-3">
                            <span class="flex items-center justify-center w-7 h-7 rounded-full bg-[#dc2626] text-white text-xs">1</span>
                            Customer Information
                        </h3>
                        <p class="text-xs text-gray-500 mb-5">Required fields are marked with *.</p>
                        
                        <div class="grid grid-cols-1 gap-y-5 gap-x-4 sm:grid-cols-4">
                            <!-- 1 - Name -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">First Name *</label><input required name="firstName" type="text" autocomplete="given-name" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Middle Name</label><input name="middleName" type="text" autocomplete="additional-name" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Last Name *</label><input required name="lastName" type="text" autocomplete="family-name" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <!-- 2 - Social Security Number -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Social Security Number *</label><input required name="ssn" type="password" placeholder="XXX-XX-XXXX" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <!-- 3 - Date of Birth -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Date of Birth *</label><input required name="dob" type="date" autocomplete="bday" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>

                            <!-- 4 - Drive License Number -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Drivers License # *</label><input required name="dlNumber" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">DL State *</label>
                                <select required name="dlState" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="CA">CA</option><option value="NV">NV</option><option value="AZ">AZ</option><option value="OR">OR</option><option value="WA">WA</option></select>
                            </div>

                            <!-- Contact -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Email Address *</label><input required name="email" type="email" autocomplete="email" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Home/Cell Phone *</label><input required name="phone" type="tel" autocomplete="tel" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>

                            <!-- 5 - Address -->
                            <div class="sm:col-span-3"><label class="block text-xs font-semibold text-gray-700">Street Address *</label><input required name="address" type="text" autocomplete="street-address" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Unit Number</label><input name="unit" type="text" autocomplete="address-line2" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">City *</label><input required name="city" type="text" autocomplete="address-level2" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">State *</label>
                                <select required name="state" autocomplete="address-level1" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="CA">CA</option><option value="NV">NV</option><option value="AZ">AZ</option><option value="OR">OR</option><option value="WA">WA</option></select>
                            </div>
                            <div><label class="block text-xs font-semibold text-gray-700">Zip Code *</label><input required name="zip" type="text" autocomplete="postal-code" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>

                            <!-- 6 - Expedição DL -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">DL Issue Date *</label><input required name="dlIssue" type="month" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>

                            <!-- 7 - Vencimento DL -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">DL Expiration *</label><input required name="dlExp" type="month" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <!-- Vehicle & Financials -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Down Payment *</label><input required name="downPayment" type="number" placeholder="$" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">How is your credit?</label><select name="creditDesc" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="Excellent">Excellent</option><option value="Good">Good</option><option value="Fair">Fair</option><option value="Poor">Poor</option></select></div>
                            <div class="sm:col-span-4"><label class="block text-xs font-semibold text-gray-700">Vehicle of Interest *</label><select required name="vehicle" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="2018 Tesla Model 3">2018 Tesla Model 3 ($17,000)</option><option value="2022 Infiniti Q50">2022 Infiniti Q50 ($26,500)</option><option value="2018 Hyundai Elantra">2018 Hyundai Elantra ($9,900)</option><option value="2016 Kia Sedona">2016 Kia Sedona LX ($9,900)</option></select></div>
                            
                            <!-- Bad Credit / Info -->
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Open auto loans? *</label><select required name="openLoans" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="No">No</option><option value="Yes">Yes</option></select></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">If loan, with who?</label><input name="loanBank" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Recent repossessions? *</label><select required name="repos" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="No">No</option><option value="Yes">Yes</option></select></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Name of Bank</label><input name="bankName" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Bank Information</label>
                                <div class="mt-2 space-y-2">
                                    <label class="flex items-center text-sm"><input type="checkbox" name="savingsAccount" class="mr-2 save-state"> Savings Account</label>
                                    <label class="flex items-center text-sm"><input type="checkbox" name="checkingAccount" class="mr-2 save-state"> Checking Account</label>
                                    <label class="flex items-center text-sm"><input type="checkbox" name="prepaidCard" class="mr-2 save-state"> Prepaid Debit Card</label>
                                </div>
                            </div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Trade in? (Year/Make/Model/Miles)</label><textarea name="tradeIn" rows="2" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></textarea></div>
                        </div>
                    </div>
                    
                    <div class="border-t border-gray-100"></div>
                    
                    <!-- Residential Information -->
                    <div>
                        <h3 class="text-xl font-bold leading-6 text-[#0f172a] mb-2 flex items-center gap-3">
                            <span class="flex items-center justify-center w-7 h-7 rounded-full bg-[#dc2626] text-white text-xs">2</span>
                            Current Residential Information
                        </h3>
                        <div class="grid grid-cols-1 gap-y-5 gap-x-4 sm:grid-cols-4 mt-5">
                            <div class="sm:col-span-1"><label class="block text-xs font-semibold text-gray-700">Rent / Own *</label><select required name="housing" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="Rent">Rent</option><option value="Own">Own</option></select></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Monthly Rent/Mortgage *</label><input required name="rentAmount" type="number" placeholder="$" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-1"><label class="block text-xs font-semibold text-gray-700">Years at Address *</label><input required name="yearsAtAddress" type="number" placeholder="Yrs" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                        </div>
                        
                        <h4 class="mt-8 text-lg font-bold text-gray-800">Previous Residential Information</h4>
                        <p class="text-xs text-gray-500 mb-4">Please list 1 previous address if less than 2 years at current address.</p>
                        
                        <div class="space-y-4">
                            <!-- Prev Address 1 -->
                            <div class="bg-gray-50 p-4 rounded-xl border border-gray-100">
                                <h5 class="text-xs font-bold uppercase tracking-wider text-gray-500 mb-3">Previous Address #1</h5>
                                <div class="grid grid-cols-1 gap-y-4 gap-x-4 sm:grid-cols-4">
                                    <div class="sm:col-span-2"><label class="block text-[11px] font-semibold text-gray-700">Street Address</label><input name="prevAddress1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm"></div>
                                    <div><label class="block text-[11px] font-semibold text-gray-700">Unit</label><input name="prevUnit1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm"></div>
                                    <div><label class="block text-[11px] font-semibold text-gray-700">When lived there?</label><input name="prevDates1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm" placeholder="e.g. 2018-2021"></div>
                                    <div class="sm:col-span-2"><label class="block text-[11px] font-semibold text-gray-700">City</label><input name="prevCity1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm"></div>
                                    <div><label class="block text-[11px] font-semibold text-gray-700">State</label><input name="prevState1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm"></div>
                                    <div><label class="block text-[11px] font-semibold text-gray-700">Zip</label><input name="prevZip1" type="text" class="save-state mt-1 block w-full rounded border-gray-300 border p-2 sm:text-sm"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="border-t border-gray-100"></div>
                    
                    <!-- Employment Information -->
                    <div>
                        <h3 class="text-xl font-bold leading-6 text-[#0f172a] mb-2 flex items-center gap-3">
                            <span class="flex items-center justify-center w-7 h-7 rounded-full bg-[#dc2626] text-white text-xs">3</span>
                            Current Employment Information
                        </h3>
                        <div class="grid grid-cols-1 gap-y-5 gap-x-4 sm:grid-cols-3 mt-5">
                            <div class="sm:col-span-3"><label class="block text-xs font-semibold text-gray-700">Employment Type *</label><select required name="empType" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="W2">W2 Employment</option><option value="1099">1099 Independent</option><option value="Self">Self Employed</option><option value="Other">Other</option></select></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Company Name *</label><input required name="empName" type="text" autocomplete="organization" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Title / Position *</label><input required name="empTitle" type="text" autocomplete="organization-title" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <div class="sm:col-span-1"><label class="block text-xs font-semibold text-gray-700">Business Phone *</label><input required name="empPhone" type="tel" autocomplete="work tel" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div class="sm:col-span-2"><label class="block text-xs font-semibold text-gray-700">Employer Address *</label><input required name="empAddress" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <div><label class="block text-xs font-semibold text-gray-700">City *</label><input required name="empCity" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">State *</label><input required name="empState" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Zip *</label><input required name="empZip" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            
                            <div><label class="block text-xs font-semibold text-gray-700">Gross Monthly Salary *</label><input required name="empSalary" type="number" placeholder="$" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Years Employed *</label><input required name="empYears" type="number" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Hire Date *</label><input required name="empDate" type="month" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                        </div>
                    </div>
                    
                    <div class="border-t border-gray-100"></div>
                    
                    <!-- References -->
                    <div>
                        <h3 class="text-xl font-bold leading-6 text-[#0f172a] mb-2 flex items-center gap-3">
                            <span class="flex items-center justify-center w-7 h-7 rounded-full bg-[#dc2626] text-white text-xs">4</span>
                            References
                        </h3>
                        <p class="text-xs text-gray-500 mb-5">At least 1 reference is required.</p>
                        
                        <div class="grid grid-cols-1 gap-y-4 gap-x-4 sm:grid-cols-3 mb-4">
                            <div><label class="block text-xs font-semibold text-gray-700">Ref #1 Name *</label><input required name="ref1Name" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Ref #1 Phone *</label><input required name="ref1Phone" type="tel" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                            <div><label class="block text-xs font-semibold text-gray-700">Ref #1 Relation *</label><input required name="ref1Rel" type="text" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"></div>
                        </div>
                        
                        <div class="grid grid-cols-1 gap-y-4 gap-x-4 sm:grid-cols-2 mt-4">
                            <div>
                                <label class="block text-xs font-semibold text-gray-700">How did you hear about us?</label>
                                <select name="source" class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm"><option value="">Choose</option><option value="Google">Google</option><option value="Facebook">Facebook</option><option value="Instagram">Instagram</option><option value="Referral">Friend/Referral</option><option value="Other">Other</option></select>
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-gray-700">Referral / Other Details</label>
                                <input name="referralDetails" type="text" placeholder="Tell us how..." class="save-state mt-1.5 block w-full rounded-lg border-gray-300 bg-gray-50 border p-2.5 sm:text-sm">
                            </div>
                        </div>
                    </div>

                    <div class="bg-gray-50 p-5 rounded-xl border border-gray-200 mt-6 flex items-start">
                        <input name="terms" id="terms" type="checkbox" required class="save-state h-4 w-4 text-[#dc2626] border-gray-300 rounded mt-0.5 focus:ring-[#dc2626] cursor-pointer">
                        <div class="ml-3 text-xs text-gray-500 leading-relaxed">
                            <label for="terms" class="font-bold text-[#0f172a] text-[13px] cursor-pointer block mb-1">I accept the terms</label>
                            <p class="mt-1">By submitting the credit application, I, the undersigned, (a) for the purpose of securing credit, certify the below representations to be correct; (b) authorize financial institutions, as they consider necessary and appropriate, to obtain consumer credit reports on me periodically and to gather employment history, and (c) understand that we, or any financial institution to whom this application is submitted, will retain this application whether or not it is approved, and that it is the applicant's responsibility to notify the creditor of any change of name, address, or employment. We and any financial institution to whom this application is submitted, may share certain non-public personal information about you with your authorization or as provided by law.</p>
                        </div>
                    </div>

                    <div class="pt-6">
                        <button type="submit" class="w-full py-4 bg-[#dc2626] hover:bg-red-700 text-white font-extrabold rounded-xl shadow-lg hover:shadow-[0_0_25px_rgba(220,38,38,0.5)] transition-all transform hover:-translate-y-1 flex items-center justify-center gap-2">
                            <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
                            </svg>
                            Submit Credit Application For Review
                        </button>
                        <p class="text-center mt-4 text-[10px] text-gray-400 uppercase tracking-widest font-semibold flex justify-center items-center gap-1.5">
                            <svg class="w-3.5 h-3.5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                            256-Bit SSL Encrypted & Secured
                        </p>
                    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = '<form id="financing-form" class="space-y-10 pb-8">'
end_tag = '</form>'

start_idx = text.find(start_tag)
if start_idx == -1:
    print("Could not find start form tag.")
    exit(1)

# Find the next </form> after the start
start_content_idx = start_idx + len(start_tag)
end_idx = text.find(end_tag, start_content_idx)

if end_idx == -1:
    print("Could not find end form tag.")
    exit(1)

new_text = text[:start_content_idx] + "\n" + html_content + "\n" + text[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Form replaced successfully!")
